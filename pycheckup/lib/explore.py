import math
from pycheckup import mongo


collection = mongo.db().repositories


def correlate(x, y):
    functions = {
        'line_count': line_count,
        'open_issues': open_issues,
        'forks': forks,
        'watchers': watchers,
        'num_collaborators': num_collaborators,
        'swearing': swearing,
        'pep8': pep8,
        'pyflakes': pyflakes
    }

    x_values = functions[x]()
    y_values = functions[y]()

    return {
        'x': x_values,
        'y': y_values,
        'r': pearson_r(x_values, y_values)
    }


def average(x):
    return float(sum(x)) / len(x)


def pearson_r(x, y):
    n = len(x)
    avg_x = average(x)
    avg_y = average(y)

    diffprod = 0
    xdiff2 = 0
    ydiff2 = 0

    for idx in range(n):
        xdiff = x[idx] - avg_x
        ydiff = y[idx] - avg_y
        diffprod += xdiff * ydiff
        xdiff2 += xdiff * xdiff
        ydiff2 += ydiff * ydiff

    return diffprod / math.sqrt(xdiff2 * ydiff2)


def line_count():
    return get_latest('line_count', 'total')


def open_issues():
    return get_latest('popularity', 'open_issues')


def forks():
    return get_latest('popularity', 'forks')


def watchers():
    return get_latest('popularity', 'watchers')


def num_collaborators():
    return get_latest('popularity', 'num_collaborators')


def swearing():
    return get_latest('swearing', 'total')


def pep8():
    return get_latest('pep8', 'total')


def pyflakes():
    return get_latest('pyflakes', 'total')


def get_latest(field, attr):
    result = []
    for d in collection.find({}, ['%s.data.%s' % (field, attr)]):
        result.append(d[field][-1]['data'][attr])

    return result
