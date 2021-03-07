from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from .models import Profileimage
from accounts import models
from accounts.models import UserInfo
from accounts.forms import UserForm

# Create your views here.
# homepage

class HomeView(TemplateView):
 
    template_name = "index.html"

