import os
from pycheckup import mapreduce


def run(repo, doc):
    doc['setup_py'] = os.path.exists(os.path.join(repo.working_dir, 'setup.py'))


def map_reduce():
    mongo.db().repositories.map_reduce(
        load_js('setup_py/map.js'),
        load_js('_common/sum_reduce.js'),
        'summary-setup-py'
    )
