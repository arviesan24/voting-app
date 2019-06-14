"""Viewsets for Votes app."""

from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django_filters import rest_framework as django_filters
from rest_framework import viewsets

from . import serializers
from . import models


class VoteFilterSet(django_filters.FilterSet):
    """Filterset for VoteViewSet."""

    def get_content_type():
        """Return list for `content_type` choices."""
        item_list = []
        # Ignore populating of dropdown list if migrations
        # look for ContentType even before it creates it.
        try:
            content_list = ContentType.objects.all()
            for item in content_list:
                item_list.append((item.name, item.name))
        except:
            pass
        return item_list

    content_type = django_filters.ChoiceFilter(
        choices=get_content_type(), field_name='content_type__model',
        lookup_expr='iexact')

    class Meta:
        model = models.Vote
        fields = ['id', 'owner', 'content_type', 'object_id']


class VoteViewSet(viewsets.ModelViewSet):
    """Viewset for VoteSerializer."""

    queryset = models.Vote.objects.all()
    serializer_class = serializers.VoteSerializer
    filter_backends = (django_filters.DjangoFilterBackend,)
    filter_class = VoteFilterSet
