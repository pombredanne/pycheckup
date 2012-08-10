from django.shortcuts import render
from pycheckup import mongo


db = mongo.db()


def index(request):
    data = {
        'popularity': {
            'watchers': watchers(),
            'collaborators': collaborators(),
            'issues': issues(),
            'forks': forks()
        },
        'features': {
            'readme': readme(),
            'license': licenses(),
            'setup_py': setup_py(),
            'tabs_spaces': tabs_spaces(),
        },
        'profane': most_profane(10)
    }

    return render(request, 'index.html', data)


#


def pluck(d, keys):
    result = {}
    for k in keys:
        if k in d:
            result[k] = d[k]

    return result


def latest(name):
    return db['summary-%s' % name].find_one(sort=[('_id', -1)])


def stats(d):
    return pluck(d, ('avg', 'min' ,'max', 'stdev'))


def grouped(name):
    result = {}
    for d in db['summary-%s' % name].find():
        result[d['_id']] = d['value']

    return result


def over_time(name, field):
    result = []

    for d in db['summary-%s' % name].find(sort=[('_id', 1)]):
        result.append({'date': d['_id'], 'value': d['value'].get(field, 0)})

    return result


#


def watchers():
    return stats(latest('popularity-watchers')['value'])


def collaborators():
    return stats(latest('popularity-collaborators')['value'])


def forks():
    return stats(latest('popularity-forks')['value'])


def issues():
    return stats(latest('popularity-issues')['value'])


def licenses():
    raw = grouped('license')
    result = []
    for license, count in raw.items():
        result.append([license, count])

    result = sorted(result, key=lambda license: license[1])
    result.reverse()
    total = sum([e[1] for e in result])

    for e in result:
        e.append((e[1] / total)*100)

    return result

def readme():
    return grouped('readme')


def setup_py():
    return grouped('setup_py')


def tabs_spaces():
    return grouped('tabs-or-spaces')


def most_profane(num):
    result = []
    for d in db['summary-profanity-score'].find(sort=[('value', -1)], limit=num):
        result.append({'repo': d['_id'], 'score': d['value']})

    return result
