from pycheckup import mongo


db = mongo.db()


def stats(user, repo):
    return db.repositories.find_one({'_id': '%s/%s' % (user, repo)})
