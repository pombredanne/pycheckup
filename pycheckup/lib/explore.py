import math
from pycheckup import mongo


collection = mongo.db().repositories


TYPES = {
    # document field, data attribute, max
    'line_count':           ('line_count', 'total', 6000000),
    'open_issues':          ('popularity', 'open_issues', 400),
    'forks':                ('popularity', 'forks', 800),
    'watchers':             ('popularity', 'watchers', 4500),
    'num_collaborators':    ('popularity', 'num_collaborators', 300),
    'swearing':             ('swearing', 'total', 6000),
    'pep8':                 ('pep8', 'total', 600000),
    'pyflakes':             ('pyflakes', 'total', 15000),
}


def distribution(name):
    if name not in TYPES:
        raise ValueError

    data = get_latest(TYPES[name][0], TYPES[name][1])
    data.sort()

    keys = get_key_range(TYPES[name][2])

    result = []
    for r in keys:
        def in_range(x): return r[0] <= x <= r[1]
        result.append((r[0], r[1], len(filter(in_range, data))))

    return {
        'data': result,
        'min': min(result, key=lambda x: x[2])[2],
        'max': max(result, key=lambda x: x[2])[2]
    }


def get_key_range(max, steps=15):
    nums = range(0, max + 1, max / steps)

    pairs = []
    prev = 0
    for n in nums[1:]:
        pairs.append((prev, n - 1))
        prev = n

    return pairs


def correlate(x, y):
    if x not in TYPES or y not in TYPES:
        raise ValueError

    x_values = get_latest(TYPES[x][0], TYPES[x][1])
    y_values = get_latest(TYPES[y][0], TYPES[y][1])

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


def get_latest(field, attr):
    result = []
    for d in collection.find({}, ['%s.data.%s' % (field, attr)]):
        result.append(d[field][-1]['data'][attr])

    return result
