import os
from pycheckup import mapreduce


def run(repo, doc):
    for root, sub_folders, files in os.walk(repo.working_dir):
        for filename in files:
            if filename.lower().startswith('readme'):
                doc['readme'] = True
                return

    doc['readme'] = False


def map_reduce():
    mapreduce.run('readme',
        map='readme/map.js',
        reduce='_common/sum_reduce.js'
    )
