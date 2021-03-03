from . import models
from django.contrib.auth.models import User, auth
from .models import UserInfo

from django.views.generic import View, TemplateView, ListView, DetailView
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
# accounts

def register(request):
 return render(request,'register.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

class UserView(DetailView):
   context_object_name = 'detail'
   model = models.UserInfo
   template_name = "user_profile.html"
   
class FeedbackView(TemplateView):
   template_name = "feedback.html"


def savedata(request):

        first_name = request.POST['firstname']
        last_name  = request.POST['lastname']
        username   = request.POST['username']
        psw        = request.POST['psw']
        psw_repeat = request.POST['psw_repeat']
        email      = request.POST['email']


        if psw != psw_repeat:
           messages.info(request,'Password Not Matching')
           return redirect('register')

        if User.objects.filter(username=username).exists():
           messages.info(request,'Username Taken')
           return redirect('register')

        elif User.objects.filter(email=email).exists():
             messages.info(request,'Email Exists')
             return redirect('register')

        else:
              user = User.objects.create_user(username=username, password=psw, email=email,first_name=first_name, last_name=last_name)
              user.save()
              print('user created')
              return redirect('/')    




def login(request):   
    
     username   = request.POST['username']
     password   = request.POST['password']


     user = auth.authenticate(username=username,password=password)


     if user is not None:
            auth.login(request,user)
            return redirect('/')
            
     else:
            messages.info(request,'Invalid Credential')
            return redirect('/')
