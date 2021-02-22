from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# accounts


class UserInfo(models.Model):
   
   user          = models.ForeignKey(User, primary_key=True, on_delete=models.CASCADE)
   phone_number  = models.CharField(max_length=12)
   gender        = models.CharField(max_length=12)
   birth_date    = models.DateField(null=True, blank=True)
   country       = models.CharField(max_length=20)
   city          = models.CharField(max_length=20)
   state         = models.CharField(max_length=20)
   address       = models.CharField(max_length=100)
   profession    = models.CharField(max_length=30)
   age           = models.IntegerField(blank=True, null=True)
   
   def __str__(self):
       return self.user.username

class Profileimages(models.Model):
    user     = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    propic   = models.ImageField(upload_to='profile_pic',blank=True)

    def __str__(self):
        return self.user.username

