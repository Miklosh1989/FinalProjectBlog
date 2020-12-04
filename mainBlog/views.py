from django.shortcuts import render
from .models import Post, Tag

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'mainBlog/index.html', context= {'posts': posts})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'mainBlog/post_detail.html', context={'posts': post})

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'mainBlog/tags_list.html', context={'tags': tags})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return  render(request, 'mainBlog/tag_detail.html', context={'tag': tag})
