import os
from pymongo import Connection


instance = None


def db():
    global instance

    if instance is None:
        mongo_uri = os.environ.get('MONGOLAB_URI')
        conn = Connection(mongo_uri)
        db_name = mongo_uri.split('/')[-1]
        instance = conn[db_name]

    return instance
