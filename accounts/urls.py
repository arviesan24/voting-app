from django.urls import include
from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('signup/', views.SignupFormView.as_view(), name='signup'),
    path('profile/', views.ProfileDetailView.as_view(), name='profile'),
]
