import os
from pycheckup import mapreduce


# Credit: https://github.com/holman/hopper
LICENSES = {
    'mit': 'Permission is hereby granted, free of charge,',
    'gpl': 'GNU GENERAL PUBLIC LICENSE',
    'lgpl': 'GNU LESSER GENERAL PUBLIC LICENSE',
    'apache': 'Apache License',
    'bsd': 'Redistribution and use in source and binary forms'
}


def run(repo, doc):
    for root, sub_folders, files in os.walk(repo.working_dir):
        for filename in files:
            if filename.lower().startswith('license'):
                doc['license'] = license_type(os.path.join(root, filename))
                return

    doc['license'] = None


def license_type(filename):
    with open(filename, 'r') as f:
        contents = f.read()

        for license, license_search in LICENSES.iteritems():
            if license_search in contents:
                return license

    return 'unknown'


def map_reduce():
    mapreduce.run(
        'license',
        map='license/map.js',
        reduce='_common/sum_reduce.js'
    )
