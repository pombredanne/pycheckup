import os
from datetime import date, datetime, timedelta
import json
from celery import Celery
from celery.utils.log import get_task_logger
import requests
from pycheckup import document, mongo
from pycheckup.git import GitRepo
from pycheckup.probes import (
    license, popularity, readme, setup_py, tabs_or_spaces,
    commits, line_count, pep8, pyflakes, swearing
)


celery = Celery('tasks', broker=os.getenv('REDISTOGO_URL', 'redis://localhost'))
logger = get_task_logger(__name__)
collection = mongo.db().repositories


@celery.task
def schedule_updates():
    # Mark all as pending
    # collection.update({}, {'$set': {'pending': True}}, multi=True)

    # Schedule each to be updated
    for r in collection.find({'pending': True}, fields=('_id'), limit=500):
        user, repo_name = r['_id'].split('/')
        working_date = datetime(year=2012, month=8, day=12)
        check_for_commits.delay(user, repo_name)


@celery.task
def check_for_commits(user, repo_name):
    print 'Checking %s/%s' % (user, repo_name)

    url = 'https://api.github.com/repos/%s/%s/commits' % (user, repo_name)
    response = requests.get(url)
    data = json.loads(response.text)

    working_date = datetime(year=2012, month=8, day=12)
    one_week_before = working_date - timedelta(days=7)

    scheduled_task = False

    for c in data:
        commit_date = datetime.strptime(
            c['commit']['author']['date'][:-6],
            '%Y-%m-%dT%H:%M:%S'
        )

        # Commit too new
        if commit_date > working_date:
            continue

        if commit_date <= working_date:
            # No new commits
            if commit_date < one_week_before:
                no_commits.delay(user, repo_name, working_date)
                scheduled_task = True
                break

            # Commit found for this week, schedule the repo to be downloaded
            else:
                update_repo.delay(user, repo_name, working_date)
                scheduled_task = True
                break

    # If by the end we still have not scheduled a task, that usually means that
    # there is more than 1 page of commits from Github that happened after our
    # working date. In such cases we schedule the repo to be downloaded and
    # run fully.
    if scheduled_task is False:
        update_repo.delay(user, repo_name, working_date)


@celery.task
def no_commits(user, repo_name, working_date):
    repo = GitRepo(user, repo_name)
    doc = collection.find_one({'_id': '%s/%s' % (user, repo_name)})
    if doc is None:
        raise Exception('%s/%s not in db!!!!!' % (user, repo_name))

    popularity.run(repo, doc, working_date)
    document.copy_last_weeks_data(doc, working_date)

    if 'pending' in doc:
        del doc['pending']

    collection.save(doc)


@celery.task
def update_repo(user, repo_name, working_date):
    repo = GitRepo(user, repo_name)
    repo.clone()
    repo.load_commits()

    doc = collection.find_one({'_id': '%s/%s' % (user, repo_name)})
    if doc is None:
        raise Exception('%s/%s not in db!!!!!' % (user, repo_name))

    popularity.run(repo, doc, working_date)

    for c in repo.commits:
        if c['date'] <= working_date:
            logger.info('Checking out %s (%s)' % (c['rev'], c['date']))
            repo.checkout(c['rev'])

            # weekly probes
            commits.run(repo, doc, working_date)
            line_count.run(repo, doc, working_date)
            pep8.run(repo, doc, working_date)
            pyflakes.run(repo, doc, working_date)
            swearing.run(repo, doc, working_date)
            break

    if 'pending' in doc:
        del doc['pending']

    collection.save(doc)
    repo.cleanup()

    print 'Finished %s/%s' % (user, repo_name)


@celery.task
def run_map_reduce():
    license.map_reduce()
    readme.map_reduce()
    setup_py.map_reduce()
    tabs_or_spaces.map_reduce()

    popularity.map_reduce()
    commits.map_reduce()
    line_count.map_reduce()
    pep8.map_reduce()
    pyflakes.map_reduce()
    swearing.map_reduce()


def remove_undefined(collection_name):
    collection = mongo.db()['summary-%s' % collection_name]

    for d in collection.find():
        if 'undefined' in d['value']:
            del d['value']['undefined']
            collection.save(d)


@celery.task
def cleanup_map_reduce():
    """
    Sometimes the map reduce jobs spit out NaNs, which cause invalid JSON.
    """
    remove_undefined('pyflakes')
    remove_undefined('pep8')
    remove_undefined('swearing')



@celery.task
def bootstrap_repo(user, repo_name):
    logger.info('Bootstraping %s/%s' % (user, repo_name))

    repo = GitRepo(user, repo_name)
    repo.clone()
    repo.load_commits()

    # doc = document.empty(user, repo_name)
    doc = collection.find_one({'_id': '%s/%s' % (user, repo_name)})
    if doc is None:
        raise Exception('%s/%s not in db!!!!!' % (user, repo_name))

    # working_date = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    working_date = datetime(year=2012, month=8, day=5)
    one_week = timedelta(days=7)

    # one-time probes
    license.run(repo, doc)
    readme.run(repo, doc)
    setup_py.run(repo, doc)
    tabs_or_spaces.run(repo, doc)

    popularity.run(repo, doc, working_date)

    current_rev = None

    if len(repo.commits) == 0:
        doc['empty'] = True
        print 'No commits in time period, skipping...'

    else:
        for _ in range(31):
            for c in repo.commits:
                if c['date'] <= working_date:
                    # Only check it out if we need to
                    if c['rev'] != current_rev:
                        logger.info('Checking out %s (%s)' % (c['rev'], c['date']))
                        repo.checkout(c['rev'])

                    current_rev = c['rev']

                    # weekly probes
                    commits.run(repo, doc, working_date)
                    line_count.run(repo, doc, working_date)
                    pep8.run(repo, doc, working_date)
                    pyflakes.run(repo, doc, working_date)
                    swearing.run(repo, doc, working_date)
                    break

            working_date -= one_week

    doc['commits'].reverse()
    doc['swearing'].reverse()
    doc['line_count'].reverse()
    doc['pep8'].reverse()
    doc['pyflakes'].reverse()

    repo_collection = mongo.db().repositories
    repo_collection.save(doc)

    repo.cleanup()

    print 'Finished %s/%s' % (user, repo_name)
