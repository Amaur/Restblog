from django.conf.urls import patterns, include, url
from .views import Index, Blog, About, Contact, Projet, Read, Recent

urlpatterns = patterns('apps.blog.views',
    # Examples:
    (r'^$',Index),
    (r'^blog$',Blog),
    (r'^contact$',Contact),
    (r'^about$',About),
    (r'^projets$',Projet),
    (r'^recent$',Recent),
    (r'^blog/(?P<slug>[^\.]+)$', Read)
    #(r'^blog/(?P<pk>[0-9]+)$', Read),(?P<slug>[^\.]+)
)