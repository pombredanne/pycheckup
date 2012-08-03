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
    mongo.db().repositories.map_reduce(
        load_js('readme/map.js'),
        load_js('_common/sum_reduce.js'),
        'summary-readme'
    )
