import os
from datetime import date, datetime, timedelta
from celery import Celery
from celery.utils.log import get_task_logger
from pycheckup import document, mongo
from pycheckup.git import GitRepo
from pycheckup.probes import license


celery = Celery('tasks', broker=os.getenv('REDISTOGO_URL', 'redis://localhost'))
logger = get_task_logger(__name__)


@celery.task
def update_repo(user, repo_name):
    pass


@celery.task
def bootstrap_repo(user, repo_name):
    logger.info('Bootstraping %s/%s' % (user, repo_name))

    repo = GitRepo(user, repo_name)
    repo.clone()
    repo.load_commits()

    # doc = document.empty(user, repo_name)
    doc = {}

    working_date = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    one_week = timedelta(days=7)

    # one-time probes
    license.run(repo, doc)

    print doc

    return




    current_rev = None

    for _ in range(52):
        for c in repo.commits:
            if c['date'] <= working_date:
                # Only check it out if we need to
                if c['rev'] != current_rev:
                    logger.info('Checking out %s' % c['rev'])
                    repo.checkout(c['rev'])

                current_rev = c['rev']

                # weekly probes
                break

        working_date -= one_week

    repo_collection = mongo.db().repositories
    repo_collection.save(doc)

    repo.cleanup()
