"""Router config for Votes APIs."""

from voting.urls import router
from . import viewsets


router.register('votes', viewsets.VoteViewSet)

urlpatterns = []
