"""Serializers for Votes app."""
from django.contrib.contenttypes.models import ContentType

from rest_framework import serializers

from . import models


class VoteSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for `Vote` model."""

    # Reference link: https://stackoverflow.com/questions/24970610/
    # set-contenttype-by-name-in-generic-relation-in-django-rest-framework
    content_type = serializers.SlugRelatedField(
        queryset=ContentType.objects.all(), slug_field='model')

    class Meta:
        model = models.Vote
        fields = (
            'url', 'id', 'owner', 'content_type', 'object_id',
            'datetime_created', 'datetime_modified')
