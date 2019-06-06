"""Viewsets for Polls app."""

from django.db.models import Q
from django_filters import rest_framework as django_filters
from rest_framework import viewsets
from rest_framework import permissions

from . import serializers
from . import models


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow poll owner to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj == request.user


class PollViewSet(viewsets.ModelViewSet):
    """Viewset for PollSerializer"""

    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer
    permission_classes = (IsOwnerOrReadOnly,)