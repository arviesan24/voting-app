from django.urls import include
from django.urls import path

from . import views


urlpatterns = [
    path('my-polls/', views.MyPollListView.as_view(), name='my-polls'),
]
