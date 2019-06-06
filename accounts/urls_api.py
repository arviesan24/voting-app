"""Router config for Accounts APIs."""

from voting.urls import router
from . import viewsets


router.register('users', viewsets.UserViewSet)

urlpatterns = []
