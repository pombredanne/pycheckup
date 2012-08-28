import json
from django.http import HttpResponse
from pycheckup import mongo
from pycheckup.lib import explore


db = mongo.db()


def json_encoder(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError, 'Could not encode %s' % type(obj)


def json_response(d):
    return HttpResponse(
        json.dumps(d, default=json_encoder),
        content_type='application/json'
    )


def mongo_time_series(name):
    return json_response([d for d in db['summary-%s' % name].find()])


def mongo_categories(name):
    result = {d['_id']: d['value'] for d in db['summary-%s' % name].find()}
    return json_response(result)


def commits_count(request):
    return mongo_time_series('commits-count')


def commits_lines(request):
    return mongo_time_series('commits-lines')


def license(request):
    return mongo_categories('license')


def line_count(request):
    return mongo_time_series('line-count')


def line_count_python(request):
    return mongo_time_series('line-count-python')


def pep8(request):
    return mongo_time_series('pep8')


def popularity_collaborators(request):
    return mongo_time_series('popularity-collaborators')


def popularity_forks(request):
    return mongo_time_series('popularity-forks')


def popularity_issues(request):
    return mongo_time_series('popularity-issues')


def popularity_watchers(request):
    return mongo_time_series('popularity-watchers')


def pyflakes(request):
    return mongo_time_series('pyflakes')


def readme(request):
    return mongo_categories('readme')


def setup_py(request):
    return mongo_categories('setup_py')


def swearing(request):
    return mongo_time_series('swearing')


def tabs_spaces(request):
    return mongo_categories('tabs-or-spaces')


def distribution(request, name):
    return json_response(explore.distribution(name))


def correlate(request, x, y):
    return json_response(explore.correlate(x, y))
