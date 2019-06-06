from django.urls import include
from django.urls import path

from . import views


urlpatterns = [
    path('my-polls/', views.MyPollListView.as_view(), name='my-polls'),
    path('details/<int:pk>/', views.PollDetailView.as_view(), name='details'),
]
