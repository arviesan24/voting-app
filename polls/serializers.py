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


class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for `Choice` model."""

    total_votes = serializers.SerializerMethodField()

    class Meta:
        model = models.Choice
        fields = (
            'url', 'id', 'poll', 'name', 'total_votes',
            'datetime_created', 'datetime_modified')
    
    def get_total_votes(self, obj):
        """Return total votes per object."""

        return obj.votes.count()
