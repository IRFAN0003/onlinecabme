from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationForm(UserCreationForm):
    is_driver = forms.BooleanField(
        required=False,
        label='Register as a driver'
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    # is_driver = forms.BooleanField(
    #     required=False,
    #     label='Login as a driver'
    # )

    class Meta:
        model = User
        fields = ['username', 'password']
