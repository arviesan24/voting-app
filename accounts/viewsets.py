"""Viewsets for Accounts app."""

from django.conf import settings
from django.db.models import Q
from django_filters import rest_framework as django_filters
from rest_framework import viewsets
from rest_framework import permissions

from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    """Viewset for UserSerializer."""

    queryset = settings.AUTH_USER_MODEL.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsAccountOwnerOrReadOnly,)
