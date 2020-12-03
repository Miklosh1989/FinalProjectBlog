from django.shortcuts import render


def posts_list(request):
    n = ["oleg", "Masha", "Olya"]
    return render(request, 'mainBlog/index.html', context= {'names': n})
