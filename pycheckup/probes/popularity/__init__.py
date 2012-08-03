import json
import requests
from pycheckup import mapreduce
from pycheckup.document import weekly_data


def run(repo, doc, end_date):
    doc['collaborators'] = collaborators(repo)

    url = 'https://api.github.com/repos/{user}/{repo_name}'.format(
        user=repo.user,
        repo_name=repo.repo_name
    )
    response = requests.get(url)
    data = json.loads(response.text)

    result = {k: data[k] for k in ('watchers', 'forks', 'open_issues')}
    result['num_collaborators'] = len(doc['collaborators'])
    doc['popularity'].append(weekly_data(end_date, result))


def collaborators(repo):
    url = 'https://api.github.com/repos/{user}/{repo}/collaborators?page={page}'

    got_all_collaborators = False
    page = 1
    collaborators = []

    while got_all_collaborators is False:
        response = requests.get(url.format(
            user=repo.user,
            repo=repo.repo_name,
            page=page
        ))
        data = json.loads(response.text)
        collaborators += [u['login'] for u in data]

        if len(data) < 30:
            got_all_collaborators = True
        else:
            page += 1

    return collaborators


def map_reduce():
    mongo.db().repositories.map_reduce(
        load_js('popularity/watchers_map.js'),
        load_js('_common/stats_reduce.js'),
        'summary-popularity-watchers',
        finalize=load_js('_common/stats_finalize.js')
    )

    mongo.db().repositories.map_reduce(
        load_js('popularity/forks_map.js'),
        load_js('_common/stats_reduce.js'),
        'summary-popularity-forks',
        finalize=load_js('_common/stats_finalize.js')
    )

    mongo.db().repositories.map_reduce(
        load_js('popularity/issues_map.js'),
        load_js('_common/stats_reduce.js'),
        'summary-popularity-issues',
        finalize=load_js('_common/stats_finalize.js')
    )

    mongo.db().repositories.map_reduce(
        load_js('popularity/collaborators_map.js'),
        load_js('_common/stats_reduce.js'),
        'summary-popularity-collaborators',
        finalize=load_js('_common/stats_finalize.js')
    )
