from django.db import models
from django.contrib import auth
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

# Create your models here.
# accounts

class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
      return "@{}".format(self.username)



class UserInfo(models.Model):
   
   user          = models.OneToOneField(auth.models.User, primary_key=True, on_delete=models.CASCADE)
   slug          = models.SlugField(allow_unicode=True, unique=True)
   phone_number  = models.CharField(max_length=12, blank=True)
   gender        = models.CharField(max_length=12, blank=True)
   birth_date    = models.DateField(null=True, blank=True)
   country       = models.CharField(max_length=20, blank=True)
   city          = models.CharField(max_length=20, blank=True)
   state         = models.CharField(max_length=20, blank=True)
   address       = models.CharField(max_length=100, blank=True)
   profession    = models.CharField(max_length=30, blank=True)
   age           = models.IntegerField(blank=True, null=True)
   propic        = models.ImageField(upload_to='profile_pic', blank=True, default='default.jpg')
   cover         = models.ImageField(upload_to='cover_photo', blank=True, default='defaultcover.png') 

   def get_absolute_url(self):
     return reverse("accounts:details", kwargs={"slug": self.slug})

   def __str__(self):
     return self.user.username

   def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

