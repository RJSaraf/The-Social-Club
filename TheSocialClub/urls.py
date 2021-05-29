from TheSocialClub import views
from django.urls import path
from django.conf.urls import url
from django.urls import reverse
from django.conf.urls import include

# TheSocialClub

app_name = 'TheSocialClub'

urlpatterns = [
    url(r"^(?P<slug>[-\w]+)/$", views.TheSocialClub.as_view(), name="home"),

    # Groups

    url(r"^group/list/$", views.ListGroups.as_view(), name="allgroup"),
    url(r"^group/create/$", views.CreateGroups.as_view(), name="creategroup"),
    url(r"^group/update/(?P<slug>[-\w]+)/$", views.UpdateGroups.as_view(), name="updategroup"),
    url(r"^posts/in_group/(?P<slug>[-\w]+)/$", views.SingleGroupsDetailView.as_view(), name="single"),
    url(r"^posts/in_friend/(?P<slug>[-\w]+)/(?P<pk>[-\w]+)/$", views.FriendsDetailView.as_view(), name="friendsingle"),
    url(r"^posts/in_friend/create/(?P<slug>[-\w]+)/(?P<pk>[-\w]+)/$", views.PrivateMessageCreateView.as_view(), name="createmsg"),
    url(r"^join/(?P<slug>[-\w]+)/$", views.JoinGroup.as_view(), name="join"),
    url(r"^leave/(?P<slug>[-\w]+)/$", views.LeaveGroup.as_view(), name="leave"),    

    # Posts

    url(r"^post/list/$", views.PostList.as_view(), name="allpost"),
    url(r"^post/(?P<username>[-\w]+)/create/$", views.CreatePost.as_view(), name="createpost"),
    url(r"post/by/(?P<username>[-\w]+)/$",views.UserPosts.as_view(),name="for_user"),
    url(r"post/by/(?P<username>[-\w]+)/(?P<pk>\d+)/$",views.PostDetail.as_view(),name="postsingle"),
    url(r"post/delete/(?P<pk>\d+)/(?P<username>[-\w]+)/$",views.DeletePost.as_view(),name="delete"),
]