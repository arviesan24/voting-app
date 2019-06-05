from django.db import models
from django.conf import settings


class Poll(models.Model):
    """Model for Polls."""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='polls',
        related_query_name='poll')
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(blank=False)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
