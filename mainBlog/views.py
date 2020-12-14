from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from django.views.generic import View
from .utils import *
from .forms import TagForm, PostForm


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'mainBlog/index.html', context= {'posts': posts})


class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'mainBlog/post_detail.html'


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'mainBlog/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'mainBlog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'mainBlog/tag_create.html'


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'mainBlog/post_create_form.html'

