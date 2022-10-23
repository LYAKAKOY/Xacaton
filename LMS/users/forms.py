from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'input__field', 'type': 'login', 'name': 'auth_login', 'placeholder': 'Kolhozniy_Pank'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'input__field', 'type': 'e-mail', 'name': 'auth_mail', 'placeholder': 'kolhozniy@gmail.com'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'input__field', 'type': 'password', 'name': 'auth_pass', 'placeholder': 'GoodPassword'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'input__field', 'type': 'password', 'name': 'auth_pass', 'placeholder': 'GoodPassword'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
