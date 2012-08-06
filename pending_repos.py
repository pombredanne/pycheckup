from pycheckup import mongo


collection = mongo.db().repositories


for r in collection.find({'swearing': []}).sort('popularity.data.watchers', -1):
    print r['_id'].replace('/', ',')

print 'Finished'
