from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import constants
from .models import Post


def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, 'index.html', {'latest_posts': latest_posts})


def all_posts(request):
    all_blog_posts = Post.objects.all().order_by("-date")
    return render(request, 'all-post.html', {"all_blog_posts": all_blog_posts})


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    post_tags = identified_post.tags.all()
    return render(request, 'detail-post.html', {'identified_post': identified_post,
                                                'post_tags': post_tags})


