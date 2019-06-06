from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import ListView

from . import models


class PollBaseListView(ListView):
    """Base ListView for Polls."""

    paginate_by = 50
    context_object_name = 'polls'


class PollListView(PollBaseListView):
    """Polls ListView."""

    template_name = 'home.html'

    def get_queryset(self):
        """Return querset for the list."""
        qs = models.Poll.objects.all().order_by('-id')
        return qs


class MyPollListView(LoginRequiredMixin, PollBaseListView):
    """Current User's Polls ListView."""

    template_name = 'polls/my-polls.html'

    def get_queryset(self):
        """Return querset for the list."""
        qs = models.Poll.objects.filter(
            owner=self.request.user).order_by('-id')
        return qs
