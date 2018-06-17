from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


# Create your views here - POSTS.

def get_posts(request): 
    blogs = Post.objects.all()
    return render(request, 'posts/posts.html', {'blogs': blogs})
