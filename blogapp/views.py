from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import constants
from .models import Post


def starting_page(request):
    latest_post = Post.objects.all().order_by("-date")[:3]
    return render(request, 'index.html', {'latest_post': latest_post})


def all_posts(request):
    all_post = Post.objects.all().order_by("-date")
    return render(request, 'all-post.html', {"all_post": all_post})


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    post_tags = identified_post.tags.all()
    return render(request, 'detail-post.html', {'identified_post': identified_post,
                                                'post_tags': post_tags})


