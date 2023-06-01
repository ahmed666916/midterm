from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


CURRENCY_CHOICES = (
    ('GBP', 'GB Pounds'),
    ('USD', 'US dollars'),
    ('EUR', 'Euros'),
)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'currency']
