from django.contrib import admin
from . import models

# Register your models here.
# TheSocialClub

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

class Message(admin.ModelAdmin):
    model = models.PrivateMessage
    list_display = 'sender', 'reciever', 'msg_content', 'created_at', 'slug'
    filter_by = 'sender', 'reciever', 'created_at', 'slug'
    list_filter = 'sender', 'reciever', 'created_at', 'slug'
    search_fields = ['sender',]
    ordering = ['created_at']

admin.site.register(models.Group)
admin.site.register(models.Post)
admin.site.register(models.FriendsList)
admin.site.register(models.FriendRequest)
admin.site.register(models.PrivateMessage)