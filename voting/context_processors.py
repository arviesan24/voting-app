"""Project custom context processors."""

from django.conf import settings

def debug(context):
    """Return DEBUG value from settings."""
    return {'DEBUG': settings.DEBUG}
