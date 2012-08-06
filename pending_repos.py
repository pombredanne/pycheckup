from pycheckup import mongo


collection = mongo.db().repositories


num = 0
for r in collection.find({'swearing': []}).sort('popularity.data.watchers', -1):
    print r['_id'].replace('/', ','), r['popularity'][0]['data']['watchers']
    num += 1


print 'Finished: %s pending.' % num
