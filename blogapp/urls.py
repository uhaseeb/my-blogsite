from django.urls import path
from . import views
urlpatterns = [
    path('', views.starting_page, name='starting_page'),
    path('all_posts/', views.all_posts, name='all_posts'),
    path('post-detail/<slug:slug>', views.post_detail, name='post_detail_page'),
]
