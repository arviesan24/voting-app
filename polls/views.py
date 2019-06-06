from django.shortcuts import render
from django.views.generic import ListView

from . import models


class PollBaseListView(ListView):
    """Base ListView for Polls."""

    paginate_by = 50
    context_object_name = 'polls'


class PollListView(ListView):
    """Polls ListView."""

    template_name = 'home.html'
    paginate_by = 50
    context_object_name = 'polls'

    def get_queryset(self):
        """Return querset for the list."""
        qs = models.Poll.objects.all().order_by('-id')
        return qs
