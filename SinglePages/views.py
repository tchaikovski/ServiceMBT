from django.views.generic import ListView, DetailView
from .models import SinglePageModel


class SinglePageView(DetailView):
    model = SinglePageModel
    template_name = 'SinglePages/singlepage.html'
    context_object_name = 'singlepage'


class BookListView(ListView):
    model = SinglePageModel
    template_name = 'SinglePages/singlrlist.html'
    # template_name = 'SinglePages/singlepage.html'

    context_object_name = 'singlelist'
    # queryset = SinglePageModel.objects.filter(title__icontains='war')[:5]
