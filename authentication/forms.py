from django import forms
from django.forms.widgets import EmailInput, PasswordInput
from authentication.models import Uzer


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=PasswordInput)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = Uzer
        fields = ['username', 'password', 'first_name', 'last_name', 'email']
