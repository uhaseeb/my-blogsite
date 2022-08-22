from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import CommentForm
from django.views.generic import ListView
from django.views import View
from django.urls import reverse


class StartingPageView(ListView):
    template_name = 'index.html'
    model = Post
    ordering = ["-date"]
    context_object_name = "latest_posts"

    def get_queryset(self):
        query_set = super().get_queryset()
        data = query_set[:3]
        return data


class AllPostsView(ListView):
    template_name = 'all-post.html'
    model = Post
    ordering = ["-date"]
    context_object_name = 'all_blog_posts'


class PostDetailView(View):
    template_name = 'detail-post.html'
    model = Post

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        stored_post = request.session.get("stored_post")

        context = {
            'post': post,
            'post_tage': post.tags.all(),
            'comment_form': CommentForm(),
            'comments': post.comments.all().order_by("-id"),
        }
        return render(request, 'detail-post.html', context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("post_detail_page", args=[slug]))
        context = {
            'post': post,
            'comment_form': comment_form,
            'post_tags': post.tags.all(),
            'comments': post.comments.all().order_by("-id")
        }
        return render(request, 'post-detail.html', context)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        print(stored_posts)
        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_post"] = False

        else:
            post = Post.objects.filter(id__in=stored_posts)
            context["posts"] = post
            context["has_post"] = True

        return render(request, 'read-later.html', context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")
        print(stored_posts)
        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
            request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/blog")

