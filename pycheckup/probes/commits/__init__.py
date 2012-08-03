from datetime import datetime, timedelta
from pycheckup import mapreduce
from pycheckup.document import weekly_data


def run(repo, doc, end_date=None):
    if end_date is None:
        end_date = datetime.utcnow()

    start_date = end_date - timedelta(days=7)
    commits = get_commits(repo, start_date, end_date)

    doc['commits'].append(weekly_data(end_date, {
        'count': len(commits),
        'lines_changed': sum([c['lines_changed'] for c in commits])
    }))


def get_commits(repo, start_date, end_date):
    weeks_commits = []

    # Starts at newest commit
    for c in repo.commits:
        # If it's too new, ignore and keep looping
        if c['date'] >= end_date:
            continue

        # If it's too old, stop
        if c['date'] < start_date:
            break

        weeks_commits.append({
            'date': c['date'],
            'lines_changed': repo.commit_num_lines_changed(c['rev'])
        })

    return weeks_commits


def map_reduce():
    mongo.db().repositories.map_reduce(
        load_js('commits/count_map.js'),
        load_js('_common/stats_reduce.js'),
        'summary-commits-count',
        finalize=load_js('_common/stats_finalize.js')
    )

    mongo.db().repositories.map_reduce(
        load_js('commits/lines_map.js'),
        load_js('_common/stats_reduce.js'),
        'summary-commits-lines',
        finalize=load_js('_common/stats_finalize.js')
    )
