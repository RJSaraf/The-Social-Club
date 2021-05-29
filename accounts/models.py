from django.db import models
from django.contrib import auth
from django.urls import reverse
from django.utils import timezone

# Create your models here.
# accounts

class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
      return "@{}".format(self.username)



class UserInfo(models.Model):
   
   user          = models.OneToOneField(auth.models.User, primary_key=True, on_delete=models.CASCADE)
   phone_number  = models.CharField(max_length=12)
   gender        = models.CharField(max_length=12)
   birth_date    = models.DateField(null=True, blank=True)
   country       = models.CharField(max_length=20)
   city          = models.CharField(max_length=20)
   state         = models.CharField(max_length=20)
   address       = models.CharField(max_length=100)
   profession    = models.CharField(max_length=30)
   age           = models.IntegerField(blank=True, null=True)
   propic   = models.ImageField(upload_to='profile_pic', blank=True, default='media/default.png')

   def get_absolute_url(self):
     return reverse("accounts:details", kwargs={"pk": self.pk})

   def __str__(self):
     return self.user.username


