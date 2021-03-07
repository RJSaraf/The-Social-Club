from django.urls import path
from django.conf.urls import url
from . import views
from . import models
from accounts.models import UserInfo
from django.contrib.auth.decorators import login_required

# accounts
app_name = 'accounts'

urlpatterns = [
path('register' , views.register, name= 'register'),
path('savedata' , views.savedata, name= 'savedata'),

url(r"^login/$", views.login, name="login"),
url(r"^logout/$", views.logout, name="logout"),
url(r"^(?P<pk>[-\w]+)/$", login_required(views.UserView.as_view()), name='details'), 
url(r"^$", views.FeedbackView.as_view(), name="feedback"),
url(r"^create/(?P<pk>[-\w]+)/$", views.UserInfoCreateView.as_view(), name="create_user_info"),
url(r"^edit/(?P<pk>[-\w]+)/$", views.UserInfoUpdateView.as_view(), name='edit_user_info'),


]