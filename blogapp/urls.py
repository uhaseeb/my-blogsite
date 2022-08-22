from django.urls import path
from . import views
urlpatterns = [
    path('', views.StartingPageView.as_view(), name='starting_page'),
    path('all_posts/', views.AllPostsView.as_view(), name='all_posts'),
    path('post-detail/<slug:slug>', views.PostDetailView.as_view(), name='post_detail_page'),
    path('read-later', views.ReadLaterView.as_view(), name='read_later')
]
