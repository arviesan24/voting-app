from django.urls import include
from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.LogoutFormView.as_view(), name='logout'),
    path('signup/', views.SignupFormView.as_view(), name='signup'),
    path('password/reset/',
        views.PasswordResetFormView.as_view(), name='password_reset'),
    path('password/change/',
        views.PasswordChangeFormView.as_view(), name='change_password'),
    path('profile/', views.ProfileDetailView.as_view(), name='profile'),
]
