from django import template

from polls import models

register = template.Library()


def total_responses(value):
    """Count all the votes from value's choices."""
    choices = models.Choice.objects.filter(poll=value)
    votes = 0
    for choice in choices:
        votes += choice.votes.count()

    return votes

register.filter('total_responses', total_responses)
