from django.urls import path
from django.conf.urls import url
from . import views
from . import models
from accounts.models import UserInfo

# accounts
app_name = 'accounts'

urlpatterns = [
path('register' , views.register, name= 'register'),
path('savedata' , views.savedata, name= 'savedata'),

url(r"^login/$", views.login, name="login"),
url(r"^logout/$", views.logout, name="logout"),
url(r"^(?P<pk>[-\w]+)/$", views.UserView.as_view(), name='details')   

]