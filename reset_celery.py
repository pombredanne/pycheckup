import os
import redis
from pycheckup import mongo
from tasks import bootstrap_repo


r = redis.from_url(os.getenv('REDISTOGO_URL', ''))
r.flushall()


print 'Flushed'


collection = mongo.db().repositories


for r in collection.find({'swearing': []}).sort('popularity.data.watchers', -1):
    user, repo = r['_id'].split('/')
    bootstrap_repo.delay(user, repo)
    print 'Scheduled %s,%s' % (user, repo)


print 'Done'
