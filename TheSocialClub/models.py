from django.db import models
from django.utils.text import slugify

from django.db import IntegrityError

# Create your models here.
# TheSocialClub

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

class Group(models.Model):
    name = models.CharField(max_length = 255, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    discription = models.TextField(blank=True, default='')
    discription_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')
    groupimage = models.ImageField(upload_to='groupimages',blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        #self.discription_html = misaka.html(self.discription)
        super().save(*args, **kwargs)

    #def get_absolute_url(self, *args, **kwargs):
        #return reverse('TheSocialClub:single', kwargs={'pk':self.kwargs.get('pk')})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name="memberships", on_delete=models.CASCADE)
    user  = models.ForeignKey(User,related_name="user_groups", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group','user')


# Posts

from django.urls import reverse
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    postimage = models.ImageField(upload_to='msgimages', blank=True)
    group = models.ForeignKey(Group,related_name='posts', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        #self.message_html = misaka.html(self.message)
        super().save(*args , **kwargs)

    class Meta:
        ordering = ['-created_at']


class FriendsList(models.Model):
    user = models.OneToOneField(User,related_name='person' , on_delete=models.CASCADE)
    friends = models.ManyToManyField(User,related_name="friendslist", blank=True)
    #message = models.ForeignKey(PrivateMessage ,related_name='person' , on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def add_friend(self, account):
        if not account in self.friends.all():
            self.friends.add(account)

    def remove_friend(self, account):
        if account in self.friends.all():
            self.friends.remove(account)

    def unfriend(self, removee):
        self.remove_friend(removee)
        friends_list = FriendsList.objects.get(user=removee)
        friends_list.remove_friend(self.user)

    def is_mutual_friend(self, friend):
        if friend in self.friends.all():
            return True
        return False

    class Meta:
        unique_together = ('user',)



class FriendRequest(models.Model):
    sender      = models.ForeignKey(User, related_name='reqsender', on_delete=models.CASCADE)
    reciever    = models.ForeignKey(User, related_name='reqreciever', on_delete=models.CASCADE)
    is_active   = models.BooleanField(blank=True, null=False, default=True)
    time        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.sender.username + '-' + self.reciever.username)

    def accept(self):

            try:
                reciever_friend_list = FriendsList.objects.get(user=self.reciever)
                if reciever_friend_list:
                    reciever_friend_list.add_friend(self.sender)

            except FriendsList.DoesNotExist:
                reciever_new_friend_list = FriendsList.objects.create(user=self.reciever)
                reciever_new_friend_list.add_friend(account=self.sender)


            try:
                sender_friend_list = FriendsList.objects.get(user=self.sender)
                if sender_friend_list:
                    sender_friend_list.add_friend(account=self.reciever)
                    self.is_active = False
                    self.save()

            except FriendsList.DoesNotExist:
                sender_new_friend_list = FriendsList.objects.create(user=self.sender)
                sender_new_friend_list.add_friend(account=self.reciever)
                self.is_active = False
                self.save()



    def decline(self):
        self.is_active = False
        self.save()

    def cancel(self):
        self.is_active = False
        self.save()


class PrivateMessage(models.Model):

    sender      = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE, blank=False)
    reciever    = models.ForeignKey(User, related_name='reciever', on_delete=models.CASCADE, blank=False)
    msg_content = models.TextField(blank=True)
    created_at  = models.DateTimeField(auto_now=True)
    image       = models.ImageField(upload_to='private_msg_img', blank=True)
    seen        = models.BooleanField(default=False)
    dilivered   = models.BooleanField(default=False)
    slug = models.SlugField(allow_unicode=True, unique=False, blank=False)

    def __str__(self):
        return (self.slug)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.sender) + '-' + str(self.reciever))
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']