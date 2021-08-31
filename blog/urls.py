from django.urls import path
from . import views
from .feeds import LastPostsFeed

app_name = 'blog'


urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('feed/', LastPostsFeed(), name='post_feed'),
    path('search/', views.post_search, name='post_search'),
]
