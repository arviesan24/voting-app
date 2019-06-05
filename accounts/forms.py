from django import forms
from allauth.account.forms import SignupForm


class UserSignupForm(SignupForm):
    """Signup form for users."""

    first_name = forms.CharField(max_length=50, label='First Name')
    last_name = forms.CharField(max_length=50, label='Last Name')

    def signup(self, request, user):
        """Save signup form value."""
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        return user
