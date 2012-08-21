from pycheckup import mongo


db = mongo.db()


def pluck(d, keys):
    result = {}
    for k in keys:
        if k in d:
            result[k] = d[k]

    return result


def latest(name):
    return db['summary-%s' % name].find_one(sort=[('_id', -1)])['value']


def stats(d):
    return pluck(d, ('avg', 'min' ,'max', 'stdev'))


def grouped(name):
    result = {}
    for d in db['summary-%s' % name].find():
        result[d['_id']] = d['value']

    return result


def percent_yes(data):
    data['percent'] = (data['yes'] / (data['yes'] + data['no'])) * 100
    return data


def over_time(name, field):
    result = []

    for d in db['summary-%s' % name].find(sort=[('_id', 1)]):
        result.append({'date': d['_id'], 'value': d['value'].get(field, 0)})

    return result


def watchers():
    return stats(latest('popularity-watchers'))


def collaborators():
    return stats(latest('popularity-collaborators'))


def forks():
    return stats(latest('popularity-forks'))


def issues():
    return stats(latest('popularity-issues'))


def licenses():
    raw = grouped('license')
    result = []
    for license, count in raw.items():
        result.append([license, count])

    # Order licenses by count
    result = sorted(result, key=lambda license: license[1])
    result.reverse()

    # Add in % of total
    total = sum([e[1] for e in result])
    for e in result:
        e.append((e[1] / total) * 100)

    return result

def readme():
    return percent_yes(grouped('readme'))


def setup_py():
    return percent_yes(grouped('setup_py'))


def tabs_spaces():
    data = grouped('tabs-or-spaces')
    total = data['tabs'] + data['spaces']
    data['percent_tabs'] = (data['tabs'] / total) * 100
    data['percent_spaces'] = (data['spaces'] / total) * 100
    return data


def other_languages():
    data = latest('line-count')
    del data['py']
    del data['total']

    result = []
    for license, count in data.items():
        result.append([license, count])

    # Order licenses by count
    result = sorted(result, key=lambda lang: lang[1])
    result.reverse()

    return result


def most_profane(num):
    result = []
    for d in db['summary-profanity-score'].find(sort=[('value', -1)], limit=num):
        result.append({'repo': d['_id'], 'score': d['value']})

    return result
