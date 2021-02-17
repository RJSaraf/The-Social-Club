from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# homepage


class Profileimage(models.Model):
    user     = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    propic   = models.ImageField(upload_to='profile_pic',blank=True)

    def __str__(self):
        return self.user.username
    