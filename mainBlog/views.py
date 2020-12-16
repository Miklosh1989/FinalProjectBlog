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


class PostCreate(ObjectCreateMixin, View):
    model_form = PostForm
    template = 'mainBlog/post_create_form.html'


class PostUpdate(ObjectUpdateMixin, View):
    model = Post
    model_form = PostForm
    template = 'mainBlog/post_update_form.html'


class PostDelete(ObjectDeleteMixin, View):
    model = Post
    template = 'mainBlog/post_delete_form.html'
    redirect_url = 'mainBlog/posts_list_url'

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'mainBlog/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'mainBlog/tag_detail.html'


class TagCreate(ObjectCreateMixin, View):
    model_form = TagForm
    template = 'mainBlog/tag_create.html'


class TagUpdate(ObjectUpdateMixin, View):
    model = Tag
    model_form = TagForm
    template = 'mainBlog/tag_update_form.html'

class TagDelete(ObjectDeleteMixin, View):
    model = Tag
    template = 'mainBlog/tag_delete_form.html'
    redirect_url = 'tags_list_url'


