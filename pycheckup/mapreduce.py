from pycheckup import mongo


def load_js(filename):
    with open('pycheckup/probes/%s' % filename, 'r') as f:
        return f.read()


def run(name, **kwargs):
    mr_kwargs = {}
    if 'finalize' in kwargs:
        mr_kwargs['finalize'] = load_js(kwargs['finalize'])

    mongo.db().repositories.map_reduce(
        load_js(kwargs['map']),
        load_js(kwargs['reduce']),
        'summary-%s' % name,
        **mr_kwargs
    )
