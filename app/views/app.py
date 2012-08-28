from django.shortcuts import render
from pycheckup.lib import project, summary


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
        'languages': summary.other_languages(),
        'profane': summary.most_profane(10)
    }

    return render(request, 'index.html', data)


def explore(request):
    return render(request, 'explore.html')


def projects(request):
    pass


def repo(request, user, repo):
    return render(request, 'project.html', {
        'user': user,
        'repo': repo,
        'data': project.stats(user, repo)
    })


def about(request):
    pass
