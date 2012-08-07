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
    mapreduce.run('swearing',
        map='swearing/count_map.js',
        reduce='swearing/count_reduce.js'
    )

    mapreduce.run('profanity-score',
        map='swearing/profane_map.js',
        reduce='swearing/profane_reduce.js'
    )
