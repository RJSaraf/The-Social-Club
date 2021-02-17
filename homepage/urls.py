from django.urls import path
from . import views
from django.conf.urls import url
from accounts import models
from accounts.models import UserInfo

# homepage
app_name = 'homepage'

urlpatterns = [
path('feedback',  views.feedback,  name= 'feedback'),
url(r"^/$", views.HomeView.as_view(), name='homepage') 

]