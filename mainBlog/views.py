from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag
from django.views.generic import View
from .utils import ObjectDetailMixin
from .forms import TagForm


def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'mainBlog/index.html', context= {'posts': posts})



class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'mainBlog/post_detail.html'

def tags_list(request):

    tags = Tag.objects.all()
    return render(request, 'mainBlog/tags_list.html', context={'tags': tags})


class TagDetail(ObjectDetailMixin,View):

    model = Tag
    template = 'mainBlog/tag_detail.html'

class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'mainBlog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'mainBlog/tag_create.html', context={'form': bound_form})