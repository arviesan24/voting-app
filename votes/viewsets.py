"""Viewsets for Votes app."""

from django.db.models import Q
from django_filters import rest_framework as django_filters
from rest_framework import viewsets

from . import serializers
from . import models


class VoteViewSet(viewsets.ModelViewSet):
    """Viewset for VoteSerializer."""

    queryset = models.Vote.objects.all()
    serializer_class = serializers.VoteSerializer