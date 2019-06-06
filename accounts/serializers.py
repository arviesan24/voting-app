"""Serializers for Accounts app."""

from django.contrib.auth import get_user_model

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for `User` model."""

    class Meta:
        model = get_user_model()
        fields = (
            'url', 'id', 'username', 'email_address', 'first_name',
            'last_name')
