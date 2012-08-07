import subprocess
from collections import defaultdict
from pycheckup import mapreduce
from pycheckup.document import weekly_data


PYFLAKES_ERRORS = {
    'UnusedImport': 'imported but unused',
    'RedefinedWhileUnused': 'redefinition of unused',
    'ImportShadowedByLoopVar': 'shadowed by loop variable',
    'ImportStarUsed': 'unable to detect undefined names',
    'UndefinedName': 'undefined name ',
    'UndefinedExport': 'in __all__',
    'UndefinedLocal': 'referenced before assignment',
    'DuplicateArgument': 'duplicate argument',
    'Redefined': 'redefinition of',
    'LateFutureImport': 'future import(s)',
    'UnusedVariable': 'is assigned to but never used'
}


def run(repo, doc, on_date):
    cmd = ['pyflakes', repo.working_dir]

    # Pyflakes violations show up in stderr.
    # If there are none, return a total of 0.
    try:
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        result = {'total': 0}
    except subprocess.CalledProcessError, e:
        result = parse_results(e.output)

    doc['pyflakes'].append(weekly_data(on_date, result))


def parse_results(results):
    violations = defaultdict(int)

    for line in results.split("\n"):
        msg = ' '.join(line.split()[1:])

        for error_name, error_search in PYFLAKES_ERRORS.iteritems():
            if error_search in msg:
                violations[error_name] += 1
                break

    violations['total'] = sum(violations.itervalues())
    return violations


def map_reduce():
    mapreduce.run('pyflakes',
        map='pyflakes/map.js',
        reduce='pyflakes/reduce.js'
    )
