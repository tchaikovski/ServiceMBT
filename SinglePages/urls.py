from django.urls import path, include
from .views import SinglePageView, BookListView

urlpatterns = [
    path('<slug:slug>/', SinglePageView.as_view(), name='singlepage'),
]
