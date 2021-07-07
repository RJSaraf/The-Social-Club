from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

from .models import Profileimage
from accounts import models
from accounts.models import UserInfo
from accounts.forms import UserForm

from TheSocialClub.models import Group, GroupMember, Post, FriendsList, FriendRequest
from django.contrib.auth.models import AnonymousUser

# Create your views here.
# homepage

class HomeView(TemplateView):
 
    template_name = "index.html"

    def get_context_data(self, *args, **kwargs):

        user = self.request.user if type(self.request.user) is not AnonymousUser else None
        try:
            
            context = super(HomeView, self).get_context_data(*args, **kwargs)
            context['friendlist'] = FriendsList.objects.filter(user_id=user.id) 
            context['friendrequest'] = FriendRequest.objects.filter(reciever=user, is_active=True)
            return context

        except :
            pass