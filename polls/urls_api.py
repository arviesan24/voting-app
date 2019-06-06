"""Router config for Polls APIs."""

from voting.urls import router
from . import viewsets


router.register('polls', viewsets.PollViewSet)

urlpatterns = []
