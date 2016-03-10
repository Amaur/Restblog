from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (PostList, PostDetail, CategoryList, CommentList,  CommentList, PostLikes, RecentPost,
                    CategoryDetail)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Restblog.views.home', name='home'),
    #url(r'^index/$',Index),
    #url(r'^users/$',UserList.as_view()),
    #url(r'^user/(?P<pk>[0-9]+)/$',UserProfil.as_view()),
    url(r'^comments/(?P<pk>[0-9]+)/$',CommentList.as_view()),
    url(r'^likes/(?P<pk>[0-9]+)/$',PostLikes.as_view()),
    url(r'^posts/$',PostList.as_view()),#Post_list),
    url(r'^recents/$', RecentPost.as_view()),
    url(r'^post/(?P<slug>[^\.]+)/$',PostDetail.as_view()),
    url(r'^categories/$',CategoryList.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/$',CategoryDetail.as_view()),
    #url(r'^login/$',LoginView.as_view()),
)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
#urlpatterns = format_suffix_patterns(urlpatterns)