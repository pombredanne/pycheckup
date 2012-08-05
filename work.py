import csv
# from tasks import bootstrap_repo
from pycheckup import mongo


collection = mongo.db().repositories


with open('data/repos.csv') as f:
    reader = csv.reader(f)

    for row in reader:user, repo = row
        r = collection.find_one({'_id': '%s/%s' % (user, repo)})
        if r is None:
            print '%s,%s' % (user, repo)
        # bootstrap_repo.delay(user, repo)

print 'Finished'
