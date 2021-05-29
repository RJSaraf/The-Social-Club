from . import models
from django.contrib import auth

from . import forms
from django.contrib.auth.models import User, auth
from TheSocialClub.forms import PostForm, GroupForm, ChatForm
from TheSocialClub.models import Group, GroupMember, Post, FriendsList
from django.db.models import Q

# Create your views here.
# TheSocialClub

from django.views import generic
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from braces.views import SelectRelatedMixin
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse_lazy
from django.urls import reverse

# Groups

from django.db import IntegrityError

class TheSocialClub(LoginRequiredMixin, generic.TemplateView):
    login_url = 'accounts:login'
    
    template_name = 'indexTSC.html'

    def get_context_data(self, *args, **kwargs):
        context = super(TheSocialClub, self).get_context_data(*args, **kwargs)
        context['grouplist'] = Group.objects.all()
        context['posts'] = Post.objects.all()
        context['form'] = PostForm
        context['friendlist'] = FriendsList.objects.filter(user_id=self.request.user.id)
        return context


class ListGroups(LoginRequiredMixin, generic.ListView):
    login_url = 'accounts:login'

    model = Group
    template_name='groups/group_listTSC.html'


class CreateGroups(LoginRequiredMixin, generic.CreateView):
    login_url = 'accounts:login'

    fields = ('name', 'discription', 'groupimage')
    model = Group
    template_name = 'groups/group_formTSC.html'


class UpdateGroups(LoginRequiredMixin, generic.UpdateView):
    login_url = 'accounts:login'
    redirect_field_name = 'TheSocialClub:single'

    form_class = GroupForm
    model = Group   
    template_name = 'groups/group_updateTSC.html'

    def get_success_url(self, *args, **kwargs):
        return reverse('TheSocialClub:single', kwargs={'slug':self.kwargs.get('slug')})

class SingleGroupsDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = 'accounts:login'
    
    model = Group
    template_name = 'groups/group_detailTSC.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SingleGroupsDetailView, self).get_context_data(*args, **kwargs)
        context['grouplist'] = Group.objects.all()
        context['form'] = PostForm
        context['friendlist'] = FriendsList.objects.filter(user_id=self.request.user.id)
        #context['ptp'] = Duo.objects.filter(Q(user1=self.request.user) | Q(user2=self.request.user))
        return context


class FriendsDetailView(LoginRequiredMixin, generic.TemplateView):
    login_url = 'accounts:login'

    template_name = 'groups/friend_detailTSC.html'

    def get_context_data(self, *args, **kwargs):
        context = super(FriendsDetailView, self).get_context_data(*args, **kwargs)
        context['grouplist'] = Group.objects.all()
        context['form'] = ChatForm
        context['friendlist'] = FriendsList.objects.filter(user_id=self.request.user.id)
        #filter(Q(user1=self.request.user) | Q(user2=self.request.user))
        
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        context['ptp'] = models.PrivateMessage.objects.filter( Q(reciever=user, sender=self.request.user) | Q(sender=user, reciever=self.request.user) )
       
        context['lastmsg'] = models.PrivateMessage.objects.filter(Q(reciever=user) | Q(sender=user)).order_by('-created_at')[:1]
       
        context['reciever'] = models.User.objects.filter(pk=self.kwargs.get('pk'))#Reciever Photo
        return context


class PrivateMessageCreateView(generic.CreateView):
    model = models.PrivateMessage
    form_class = ChatForm

    def form_valid(self, form, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        form = form.save(commit=False)
        form.sender = self.request.user
        form.reciever = user
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self, *args, **kwargs):
        pk=self.kwargs.get('pk')
        slug=self.kwargs.get('slug')
        return reverse("TheSocialClub:friendsingle", kwargs={"pk": pk, 'slug':slug})


class JoinGroup(LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('TheSocialClub:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(Group, slug=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request,('Warning already a member!'))
        else:
            messages.success(self.request, 'You are now a member!')

        return super().get(request, *args, **kwargs)

class LeaveGroup (LoginRequiredMixin, generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
            return reverse('TheSocialClub:single', kwargs={'slug':self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):

        try:
            membership = models.GroupMember.objects.filter(

                user=self.request.user,
                group__slug=self.kwargs.get('slug')

            ).get()

        except models.GroupMember.DoesNotExist:
                messages.warning(self.request, 'Sorry you are not in this group!')
        else:
            membership.delete()
            messages.success(self.request, 'You Have Left the group!')
        return super().get(request, *args, **kwargs)



# Posts

from django.http import Http404
from braces.views import SelectRelatedMixin

from django.contrib.auth import get_user_model
User = get_user_model()

class PostList(SelectRelatedMixin, generic.ListView):

    template_name = 'posts/post_listTSC.html'
    model = models.Post
    select_related = ('user', 'group')


class UserPosts(generic.ListView):

    model = models.Post
    template_name = 'posts/user_post_listTSC.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
    
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_user"] = self.post_user
        return context
    

class PostDetail(SelectRelatedMixin, generic.DetailView):
    model = models.Post
    select_related = ('user', 'group')
    template_name = 'posts/post_detailTSC.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))


class CreatePost(SelectRelatedMixin, LoginRequiredMixin, generic.CreateView):
    login_url = '/'
    model = models.Post
    fields = ('message', 'postimage')

    def form_valid(self, form, *args, **kwargs):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        self.object = form.save(commit=False)
        self.object.user = user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse("TheSocialClub:home", kwargs={"slug": self.kwargs.get('username')})


'''
    def dispatch(self, request, *args, **kwargs):
        self.group = get_object_or_404(Group, pk=kwargs['pk'])
        return super(CreatePost, self).dispatch(request, *args, **kwargs)
'''


class DeletePost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):

    model = models.Post
    select_related = ('user', 'group')
    template_name = 'posts/post_confirm_deleteTSC.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'post Deleted')
        return super().delete(*args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        return reverse("TheSocialClub:home", kwargs={"slug": self.kwargs.get('username')})