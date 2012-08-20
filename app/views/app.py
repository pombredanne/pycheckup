from django.http import HttpResponse
from django.shortcuts import render
from pycheckup.lib import summary


def index(request):
    data = {
        'popularity': {
            'watchers': summary.watchers(),
            'collaborators': summary.collaborators(),
            'issues': summary.issues(),
            'forks': summary.forks()
        },
        'features': {
            'readme': summary.readme(),
            'license': summary.licenses(),
            'setup_py': summary.setup_py(),
            'tabs_spaces': summary.tabs_spaces(),
        },
        'profane': summary.most_profane(10)
    }

    return render(request, 'index.html', data)


def projects(request):
    pass


def repo(request, user, repo):
    return HttpResponse('%s / %s' % (user, repo))


def about(request):
    pass
