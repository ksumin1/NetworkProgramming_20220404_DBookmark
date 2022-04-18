from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from bookmark.models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    # bookmark_list.html, {'bookmark_list': Bookmark.objects.all()}

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['name', 'url']
    template_name_suffix = '_create'                # Bookmark_from.html -> bookmark_create.html
    success_url = reverse_lazy('bookmark:list')


class BookmarkDetailView(DetailView):
    model = Bookmark