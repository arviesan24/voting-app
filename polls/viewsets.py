"""Viewsets for Polls app."""

from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django_filters import rest_framework as django_filters
from rest_framework import viewsets
from rest_framework import permissions

from . import serializers
from . import models

from votes.models import Vote


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
        return obj.owner == request.user


class IsChoiceOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow choice owner to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.poll.owner == request.user


class PollFilterSet(django_filters.FilterSet):
    """FilterSet for PollViewSet."""

    class Meta:
        model = models.Poll
        fields = ['id', 'owner', 'title', 'description']


class ChoiceFilterSet(django_filters.FilterSet):
    """FilterSet for ChoiceViewSet."""

    class Meta:
        model = models.Choice
        fields = ['id', 'poll', 'name']


class PollViewSet(viewsets.ModelViewSet):
    """Viewset for PollSerializer."""

    queryset = models.Poll.objects.all()
    serializer_class = serializers.PollSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = PollFilterSet


class ChoiceViewSet(viewsets.ModelViewSet):
    """Viewset for ChoiceSerializer."""

    queryset = models.Choice.objects.all()
    serializer_class = serializers.ChoiceSerializer
    permission_classes = (IsChoiceOwnerOrReadOnly,)
    filter_backends = (django_filters.DjangoFilterBackend,)
    filterset_class = ChoiceFilterSet

    def destroy(self, request, pk=None):
        """Execute when delete request has been made."""
        # select Votes related to Choice
        content_type = ContentType.objects.get_for_model(models.Choice)
        choice_votes = Vote.objects.filter(
            content_type=content_type, object_id=pk)
        # delete selected Votes
        choice_votes.delete()

        return super().destroy(request, pk)
