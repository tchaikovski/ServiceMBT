from django.urls import path, include
from .views import single_page_detail

urlpatterns = [
    # path('<slug:post>/', views.post_detail, name='post_detail'),
    # path('<slug:slug>/', SinglePageView.as_view(), name='singlepage'),
    path('<slug:post>/', single_page_detail, name='singlepage'),
]
