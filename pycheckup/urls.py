from django.conf.urls.defaults import patterns


urlpatterns = patterns('',
    (r'^$', 'pycheckup.views.app.index'),
)
