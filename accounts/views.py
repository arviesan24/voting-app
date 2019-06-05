"""Accounts app view."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

from allauth.account.forms import LoginForm
from allauth.account.views import LoginView
from allauth.account.views import PasswordChangeView
from allauth.account.views import PasswordResetView
from allauth.account.views import SignupView

from . import forms

class LoginFormView(LoginView):
    """User login view."""

    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:profile')


class LogoutFormView(LogoutView):
    """User logout view."""

    template_name = 'accounts/logout.html'


class SignupFormView(SignupView):
    """User signup view."""

    form_class = forms.UserSignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')


class ProfileDetailView(LoginRequiredMixin, DetailView):
    """Profile view of the user."""

    template_name = 'accounts/profile.html'

    def get_object(self):
        """Return object to be displayed by view."""
        return self.request.user


class PasswordResetFormView(PasswordResetView):
    """View for Reset Password."""

    template_name = 'accounts/password_reset.html'


class PasswordChangeFormView(LoginRequiredMixin, PasswordChangeView):
    """View for change Password."""

    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('accounts:profile')
