from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Restblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include('apps.blog.urls')),
    url(r'^api/',include('apps.api.v1.urls',namespace='v1')),
    #url(r'^v2/',include('apps.api.v2.urls',namespace='v2')),
    #url(r'^account/',include('apps.account.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^markdown/',include("django_markdown.urls"))
    
    
)
