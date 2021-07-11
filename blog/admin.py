from django.contrib import admin
from blog.models import Post, Comment
from haystack.admin import SearchModelAdmin

# Register your models here.
# blog


class PostModelAdmin(SearchModelAdmin):
    haystack_connection = 'whoosh'
    list_display = ('author', 'title', 'text')
    date_hierarchy = 'published_date'


admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment)