import os
from collections import defaultdict
from pycheckup import mapreduce
from pycheckup.document import weekly_data


CODE_EXTENSIONS = (
    'py', 'html', 'css', 'scss', 'js', 'coffee', 'txt', 'xml', 'yaml', 'yml',
    'csv', 'sql', 'c', 'h', 'cpp', 'm', 'sh', 'php', 'rb', 'pl', 'java', 'clj'
)


def run(repo, doc, on_date):
    doc['line_count'].append(weekly_data(on_date, get_counts(repo)))


def get_counts(repo):
    counts = defaultdict(int)

    for root, sub_folders, files in os.walk(repo.working_dir):
        for filename in files:
            if '.' in filename:
                ext = filename.lower().split('.')[-1]

                if ext in CODE_EXTENSIONS:
                    with open(os.path.join(root, filename), 'r') as f:
                        counts[ext] += sum(1 for line in f)

    counts['total'] = sum(counts.itervalues())
    return counts


def map_reduce():
    mongo.db().repositories.map_reduce(
        load_js('line_count/count_map.js'),
        load_js('line_count/count_reduce.js'),
        'summary-line-count'
    )

    mongo.db().repositories.map_reduce(
        load_js('line_count/python_map.js'),
        load_js('_common/stats_reduce.js'),
        'summary-line-count-python',
        finalize=load_js('_common/stats_finalize.js')
    )
