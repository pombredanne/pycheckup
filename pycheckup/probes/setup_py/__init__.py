import os
from pycheckup import mapreduce


def run(repo, doc):
    doc['setup_py'] = os.path.exists(os.path.join(repo.working_dir, 'setup.py'))


def map_reduce():
    mapreduce.run('setup_py',
        map='setup_py/map.js',
        reduce='_common/sum_reduce.js',
    )
