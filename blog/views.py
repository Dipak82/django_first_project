
from django.shortcuts import render

from blog.models import Post


def home(request):
    context = {'titles': 'HOME', 'post': Post.objects.all()}
    return render(request, 'blog/home.html', context )


def about(request):
    return render(request, 'blog/about.html', {'titles':'About'})