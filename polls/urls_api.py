"""Router config for Polls APIs."""

from voting.urls import router
from . import viewsets


router.register('choices', viewsets.ChoiceViewSet)
router.register('polls', viewsets.PollViewSet)

urlpatterns = []
