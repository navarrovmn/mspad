from django import forms
from django.contrib.auth.models import User


class SignupForm(forms.ModelForm):

    password = forms.CharField(
        label=('Password'),
        required=True,
        widget=forms.PasswordInput,
    )

    password_confirm = forms.CharField(
        label=('Password confirmation'),
        required=True,
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields=['username']
