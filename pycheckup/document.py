


def empty(user, repo_name):
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
