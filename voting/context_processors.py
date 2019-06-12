"""Project custom context processors."""

from django.conf import settings

from rest_framework.authtoken.models import Token


def global_custom_tags(context):
    """Returns additional context to templates."""
    return {'DEBUG': settings.DEBUG, 'API_ROOT_URL': settings.API_ROOT_URL}
