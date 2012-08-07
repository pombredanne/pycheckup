from django.conf.urls.defaults import patterns


urlpatterns = patterns('',
    (r'^$', 'app.views.app.index'),
)
