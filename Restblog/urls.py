from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Restblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include('apps.blog.urls')),
    url(r'^api/v1/',include('apps.api.urls')),
    url(r'^account/',include('apps.account.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/',include("django_markdown.urls"))
    
    
)
