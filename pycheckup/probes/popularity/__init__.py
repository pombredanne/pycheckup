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
    url = 'https://api.github.com/repos/{user}/{repo}/collaborators'

    response = requests.get(url.format(
        user=repo.user,
        repo=repo.repo_name
    ))
    data = json.loads(response.text)
    return [u['login'] for u in data]


def map_reduce():
    mapreduce.run('popularity-watchers',
        map='popularity/watchers_map.js',
        reduce='_common/stats_reduce.js',
        finalize='_common/stats_finalize.js'
    )

    mapreduce.run('popularity-forks',
        map='popularity/forks_map.js',
        reduce='_common/stats_reduce.js',
        finalize='_common/stats_finalize.js'
    )

    mapreduce.run('popularity-issues',
        map='popularity/issues_map.js',
        reduce='_common/stats_reduce.js',
        finalize='_common/stats_finalize.js'
    )

    mapreduce.run('popularity-collaborators',
        map='popularity/collaborators_map.js',
        reduce='_common/stats_reduce.js',
        finalize='_common/stats_finalize.js'
    )
