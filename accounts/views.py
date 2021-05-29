from . import models
#from django.contrib.auth.models import User, auth

from django.contrib import auth
from accounts.models import UserInfo
from accounts.forms import UserForm
from . import forms

from django.views.generic import View, TemplateView, ListView, DetailView,CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse_lazy
from django.urls import reverse


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


class UserInfoCreateView(CreateView):
     login_url = '/'
     redirect_field_name = 'user_profile.html'
     
     model = models.UserInfo
     form_class = UserForm
     template_name = "EditUserInfo.html"


     def form_valid(self, form):
        article = form.save(commit=False)
        article.user = self.request.user
        #article.save()  # This is redundant, see comments.
        return super(UserInfoCreateView, self).form_valid(form)



class UserInfoUpdateView(UpdateView):
     login_url = '/'
     redirect_field_name = 'user_profile.html'
     
     model = models.UserInfo
     form_class = UserForm
     template_name = "EditUserInfo.html"


class SignUp(CreateView):
   
   form_class = forms.UserCreateForm
   success_url = reverse_lazy('accounts:login')
   template_name = 'signup.html'
