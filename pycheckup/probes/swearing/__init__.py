import subprocess
from collections import defaultdict
from pycheckup import mapreduce
from pycheckup.document import weekly_data


# (abridged)
SWEAR_WORDS = [
    'shit',
    'shitty',
    'fuck',
    'fucked',
    'fucking',
    'ass',
    'asshole',
    'cunt',
]


def run(repo, doc, on_date):
    counts = defaultdict(int)

    for word in SWEAR_WORDS:
        cmd = ['grep', word, '-rw', repo.working_dir]

        try:
            output = subprocess.check_output(cmd)
            # results += output.split("\n")
            counts[word] = len(filter(bool, output.split("\n")))
        except subprocess.CalledProcessError:
            pass

    counts['total'] = sum(counts.itervalues())
    doc['swearing'].append(weekly_data(on_date, counts))


def map_reduce():
    mongo.db().repositories.map_reduce(
        load_js('swear/count_map.js'),
        load_js('swear/count_reduce.js'),
        'summary-swearing'
    )

    mongo.db().repositories.map_reduce(
        load_js('swear/profane_map.js'),
        load_js('swear/profane_reduce.js'),
        'summary-profanity-score'
    )
