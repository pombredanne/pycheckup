import json
from pycheckup import mongo


db = mongo.db()


def json_encoder(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError, 'Could not encode %s' % type(obj)


def stats(user, repo):
    doc = db.repositories.find_one({'_id': '%s/%s' % (user, repo)})
    doc['commits'] = json.dumps(doc['commits'], default=json_encoder)
    doc['line_count'] = json.dumps(doc['line_count'], default=json_encoder)
    doc['pep8'] = json.dumps(doc['pep8'], default=json_encoder)
    doc['pyflakes'] = json.dumps(doc['pyflakes'], default=json_encoder)
    doc['swearing'] = json.dumps(doc['swearing'], default=json_encoder)
    return doc
