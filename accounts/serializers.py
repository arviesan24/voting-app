"""Serializers for Accounts app."""

from django.conf import settings

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for `User` model."""

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = (
            'url', 'id', 'username', 'email_address', 'first_name',
            'last_name')
