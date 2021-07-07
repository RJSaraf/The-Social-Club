import datetime
from haystack import indexes

from TheSocialClub import models
from blog.models import Post
from accounts import models
from django.contrib.auth.models import User

class UserIndex(indexes.SearchIndex, indexes.Indexable):
    
    text = indexes.CharField(document=True, use_template=True)
    username = indexes.CharField(model_attr='username')
    first_name = indexes.CharField(model_attr='first_name')
    last_name = indexes.CharField(model_attr='last_name')
    email = indexes.CharField(model_attr='email')

    def get_model(self):
        return User

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class PostIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='author')
    title = indexes.CharField(model_attr='title')
    texts = indexes.EdgeNgramField(model_attr='text')

    def get_model(self):
        return Post

