import csv
from tasks import bootstrap_repo


with open('data/repos100.csv') as f:
   reader = csv.reader(f)

   for row in reader:
       user, repo = row
       bootstrap_repo.delay(user, repo)

print 'Finished'
