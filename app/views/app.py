import os
from django.http import HttpResponse
from django.shortcuts import render
from postmark import PMMail
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
    return render(request, 'projects.html')


def repo(request, user, repo):
    return render(request, 'project.html', {
        'user': user,
        'repo': repo,
        'data': project.stats(user, repo)
    })


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        mailer = PMMail(
            to=os.environ.get('POSTMARK_RECEIVER'),
            subject='Pycheckup: %s' % request.POST['email'],
            text_body="Email: %s\nWebsite: %s\n\n%s" % (
                request.POST['email'],
                request.POST['website'],
                request.POST['description'],
            )
        )
        mailer.send()

    return HttpResponse('OK')
