import os
from pycheckup import mapreduce


def run(repo, doc):
    total_tabs = 0
    total_spaces = 0

    for filename in get_repo_python_files(repo.working_dir):
        try:
            with open(filename, 'r') as f:
                contents = f.read()

                num_tabs = contents.count("\t")
                num_four_spaces = contents.count('    ')
                num_two_spaces = contents.count('  ') - (num_four_spaces * 2)

                total_tabs += num_tabs
                total_spaces += num_two_spaces + num_four_spaces
        except IOError:
            pass

    if total_tabs >= total_spaces:
        doc['tabs_or_spaces'] = 'tabs'
    else:
        doc['tabs_or_spaces'] = 'spaces'


def get_repo_python_files(working_dir):
    file_list = []

    for root, sub_folders, files in os.walk(working_dir):
        for filename in files:
            if filename.endswith('.py'):
                file_list.append(os.path.join(root, filename))

    return file_list


def map_reduce():
    mongo.db().repositories.map_reduce(
        load_js('tabs_or_spaces/map.js'),
        load_js('_common/sum_reduce.js'),
        'summary-tabs-or-spaces'
    )
