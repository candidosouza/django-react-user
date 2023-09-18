from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm



class LoginForm(forms.Form):
    username = forms.EmailField(
        label='Email',
        max_length=254,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )
    password = forms.CharField(
        label='Senha',
        required=True,
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Senha',
                'autocomplete': 'current-password'
            }
        )
    )

    class Meta:
        model = User


class RegisterForm(UserCreationForm):
    name = forms.CharField(
        label='Nome',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Nome'
            }
        )
    )
    email = forms.CharField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )
    password1 = forms.CharField(
        label='Password',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Senha'
            }
        )
    )
    password2 = forms.CharField(
        label='Confirmar senha',
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirmar senha'
            }
        )
    )

    class Meta:
        model = User
        fields = ['name', 'email', 'password1', 'password2']
    