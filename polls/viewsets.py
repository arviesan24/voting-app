"""Viewsets for Polls app."""

from django.db.models import Q
from django_filters import rest_framework as django_filters
from rest_framework import viewsets
from rest_framework import permissions

from . import serializers
from . import models


class PollViewSet(viewsets.ModelViewSet):
    """Viewset for PollSerializer"""

    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer
    permission_classes = (IsOwnerOrReadOnly,)
