from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation


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


class Choice(models.Model):
    """Model for Poll choices."""

    poll = models.ForeignKey('Poll', on_delete=models.CASCADE,
        related_name='choices',
        related_query_name='choice')
    name = models.TextField(blank=False)
    votes = GenericRelation(Vote)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
