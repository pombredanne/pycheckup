import subprocess
from collections import defaultdict
from pycheckup import mapreduce
from pycheckup.document import weekly_data


def run(repo, doc, on_date):
    cmd = ['pep8', repo.working_dir, '-r']

    # pep8 violations show up in stderr.
    # If there are none, return a total of 0.
    try:
        subprocess.check_output(cmd)
        result = {'total': 0}
    except subprocess.CalledProcessError, e:
        result = parse_results(e.output)

    doc['pep8'].append(weekly_data(on_date, result))


def parse_results(results):
    violations = defaultdict(int)

    for line in results.split("\n"):
        try:
            violations[line.split()[1]] += 1
        except IndexError:
            pass

    violations['total'] = sum(violations.itervalues())
    return violations


def map_reduce():
    mongo.db().repositories.map_reduce(
        load_js('pep8/map.js'),
        load_js('pep8/reduce.js'),
        'summary-pep8'
    )
