


def empty(user, repo_name):
    if '.' in repo_name:
        repo_name = repo_name.replace('.', '_')

    return {
        '_id': '%s/%s' % (user, repo_name),
        'license': None,
        'readme': False,
        'setup_py': False,
        'tabs_or_spaces': 'spaces',
        'created_at': None,
        'collaborators': [],
        'commits': [],
        'popularity': [],
        'swearing': [],
        'line_count': [],
        'pep8': [],
        'pyflakes': []
    }


def weekly_data(on_date, data):
    return {
        'date': on_date,
        'data': data
    }


def copy_last_weeks_data(doc, on_date):
    doc['commits'].append(weekly_data(on_date, {'count': 0, 'lines_changed': 0}))

    doc['swearing'].append(weekly_data(on_date, doc['swearing'][-1]['data']))
    doc['line_count'].append(weekly_data(on_date, doc['line_count'][-1]['data']))
    doc['pep8'].append(weekly_data(on_date, doc['pep8'][-1]['data']))
    doc['pyflakes'].append(weekly_data(on_date, doc['pyflakes'][-1]['data']))

    return doc
