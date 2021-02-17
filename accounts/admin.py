from django.contrib import admin
from .models import UserInfo, Profileimages

# Register your models here.
# accounts

admin.site.register(UserInfo)
admin.site.register(Profileimages)