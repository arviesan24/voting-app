"""Accounts app view."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from allauth.account.forms import LoginForm
from allauth.account.views import SignupView

from . import forms

class LoginFormView(FormView):
    """User login view."""

    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:profile')


class SignupFormView(SignupView):
    """User signup view."""

    form_class = forms.UserSignupForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:login')
