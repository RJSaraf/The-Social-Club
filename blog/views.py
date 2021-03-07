from . import models  
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.contrib.auth.models import User, auth

from django.views.generic import View, TemplateView, ListView, DetailView,CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse_lazy
from django.urls import reverse

# Create your views here.
# blog


class PostListView(ListView):
    context_object_name = 'posts'
    model = Post
    template_name='post_list.html'
    # feild lookups django __lte
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    

class PostDetailView(DetailView):
    context_object_name = 'posts'
    model = models.Post 
    template_name = 'post_detail.html'


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/'
    redirect_field_name = 'post_detail.html'
    
    model = models.Post
    form_class = PostForm
    template_name = 'post_form.html' 


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/'
    redirect_field_name = 'post_detail.html'
    
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
    template_name = 'post_confirm_delete.html'


class DraftListView(LoginRequiredMixin, ListView):
    login_url = '/'
    redirect_field_name = 'post_list.html'

    model = Post
    template_name = 'post_draft_list.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('-created_date')
    
################################################################################################################################################

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('blog:post_detail',pk=pk)


@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'comment_form.html',{'form':form})            


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('blog:post_detail',pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post_detail',pk=post_pk)
