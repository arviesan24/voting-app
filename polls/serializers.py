"""Serializers for Polls app."""

from rest_framework import serializers

from . import models


class PollSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for `Poll` model."""

    class Meta:
        model = models.Poll
        fields = (
            'url', 'id', 'owner', 'title', 'description',
            'datetime_created', 'datetime_modified')
