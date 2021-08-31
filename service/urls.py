from django.urls import path
from . import views
from django.views.decorators.cache import cache_page

app_name = 'service'

urlpatterns = [
    # path('', views.PostListView.as_view(), name='post_list'),
    # path('<slug:post>/', views.post_detail, name='post_detail'),
    # path('<int:post_id>/share/', views.post_share, name='post_share'),
    # path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    # path('feed/', LastPostsFeed(), name='post_feed'),
    # path('search/', views.post_search, name='post_search'),
    # path('contact/', views.ContactFormView.as_view(), name='contact'),
    path('', views.ServiceHome.as_view(), name='home'),
    path('<slug:first_slug>/', views.FirstPageServiceView.as_view(), name='first_page'),
    # path('<slug:cat_slug>/', views.ServiceCategoryView.as_view(), name='category'),
    path('post/<slug:post>/', views.page_service_detail, name='page_service_detail'),
    # path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),

]

from django.urls import path, re_path
from django.views.decorators.cache import cache_page

from .views import *

# urlpatterns = [
# path('', ServiceHome.as_view(), name='home'),
# path('about/', about, name='about'),
# path('addpage/', AddPage.as_view(), name='add_page'),
# path('contact/', ContactFormView.as_view(), name='contact'),
# path('login/', LoginUser.as_view(), name='login'),
# path('logout/', logout_user, name='logout'),
# path('register/', RegisterUser.as_view(), name='register'),
# path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
# path('<slug:cat_slug>/', ServiceCategoryView.as_view(), name='category'),
# ]
