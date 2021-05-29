from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.
# blog

class Post(models.Model):
    author         = models.ForeignKey(User, on_delete=models.CASCADE)
    title          = models.CharField(max_length=200)
    text           = models.TextField()
    created_date   = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    postimage      = models.ImageField(upload_to='blog/media/postimages',blank=True,default='defaultpost.jpg')
    like           = models.ManyToManyField(User,related_name='likepost',null=True)
    dislike        = models.ManyToManyField(User,related_name='dislikepost',null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comments=True)

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})


    def dislikepost(self):
        self.dislike = request.user
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey( 'blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comments = models.BooleanField(default=False)
    like           = models.ManyToManyField(User,related_name='likecomment')
    dislike        = models.ManyToManyField(User,related_name='dislikecomment')

    def approve(self):
        self.approved_comments = True
        self.save()

    def get_absolute_url(Comment):
        return reverse("blog:post_detail", kwargs={"pk": Comment.post.pk})

    
    
    def __str__(self):
        return self.text
        













    
