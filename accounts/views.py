from .models import UserInfo
from django.contrib.auth.models import User

from django.contrib import auth
from accounts.models import UserInfo
from accounts.forms import UserForm
from . import forms

from TheSocialClub.forms import PostForm, GroupForm, ChatForm
from TheSocialClub.models import Group, GroupMember, Post, FriendsList, FriendRequest
from blog import models

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

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')


class UserView(DetailView, LoginRequiredMixin):
   login_url = 'accounts:login'

   context_object_name = 'user'
   model = UserInfo
   template_name = "user_profile.html"
       
   def is_friend(self):
      user = get_object_or_404(User, username=self.kwargs.get('slug'))
      try:
         FL= FriendsList.objects.get(user=user)
         if self.request.user in FL.friends.all():
            return True
         else:
            return False

      except FriendsList.DoesNotExist:
         return False

   def is_active(self):
      user = get_object_or_404(User, username=self.kwargs.get('slug'))
      if FriendRequest.objects.filter(sender=self.request.user, reciever=user, is_active=True).exists():
         return True
      else:
         return False
            
   def get_context_data(self, *args, **kwargs):
      user = get_object_or_404(User, username=self.kwargs.get('slug'))
      Friends = get_object_or_404(FriendsList, user=user).friends.all().order_by('id')[:9]
      blogcount = models.Post.objects.filter(author=user).count()

      context = super(UserView, self).get_context_data(*args, **kwargs)
      context['blogcount'] = blogcount
      context['limitedbloglist'] = models.Post.objects.filter(author=user)[:9]
      context['posts'] = Post.objects.filter(user=user)
      context['form'] = PostForm
      context['friendlist'] = FriendsList.objects.filter(user=user)
      context['limitedfriendlist'] = Friends #friendslist
      context['sentfriendrequest'] = FriendRequest.objects.filter(sender=self.request.user, reciever=user, is_active=True) # Cancel Request
      context['is_active'] = {"yn" : self.is_active()} # Add Friend
      context['friendrequest'] = FriendRequest.objects.filter(reciever=self.request.user, is_active=True) #For Navbar
      context['is_friend'] = {"isf" : self.is_friend()} # Is Friend 
      return context

   
class FeedbackView(TemplateView):
   template_name = "feedback.html"


class UserInfoCreateView(CreateView):
     login_url = '/'
     redirect_field_name = 'user_profile.html'
     
     model = UserInfo
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
     
     model = UserInfo
     form_class = UserForm
     template_name = "EditUserInfo.html"


class SignUp(CreateView):
   
   form_class = forms.UserCreateForm
   success_url = reverse_lazy('accounts:login')
   template_name = 'signup.html'
