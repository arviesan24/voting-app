"""Viewsets for Accounts app."""

from django.contrib.auth import get_user_model
from django.db.models import Q
from django_filters import rest_framework as django_filters
from rest_framework import viewsets
from rest_framework import permissions

from . import serializers


class IsAccountOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only the account owner to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj == request.user


class UserViewSet(viewsets.ModelViewSet):
    """Viewset for UserSerializer."""

    queryset = get_user_model().objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (
        permissions.IsAuthenticated, IsAccountOwnerOrReadOnly,)
