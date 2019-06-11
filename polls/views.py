"""Views for polls app."""

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView


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


class PollDetailView(DetailView):
    """Displays poll details."""

    template_name = 'polls/details.html'
    model = models.Poll
    context_object_name = 'poll'


class PollUpdateView(LoginRequiredMixin, UpdateView):
    """View to update Poll."""

    template_name = 'polls/update.html'
    model = models.Poll
    fields = ['title', 'description']
    context_object_name = 'poll'

    def get_success_url(self):
        """Return success URL."""
        return reverse_lazy(
            'polls:update', kwargs = {'pk' : self.object.id, })

    def form_valid(self, form):
        """Actions done on form success."""
        messages.success(self.request, 'Poll details updated.')

        return super().form_valid(form)
