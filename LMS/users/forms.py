from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    """Форма для регистрации пользователя"""
    username = forms.CharField(label='Логин', widget=forms.TextInput(
        attrs={'class': 'input__field', 'type': 'login', 'name': 'auth_login', 'placeholder': 'Kolhozniy_Pank'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'input__field', 'type': 'e-mail', 'name': 'auth_mail', 'placeholder': 'kolhozniy@gmail.com'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'input__field', 'type': 'password', 'name': 'auth_pass', 'placeholder': 'GoodPassword'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(
        attrs={'class': 'input__field', 'type': 'password', 'name': 'auth_pass', 'placeholder': 'GoodPassword'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class AuntificationUserForm(AuthenticationForm):
    """Форма для аутентификации пользователя"""

    username = forms.CharField(label='Логин',
                               widget=forms.TextInput(attrs={'type': 'login', 'class': 'input__field',
                                                             'name': 'auth_login',
                                                             'placeholder': 'Kolhozniy_Pank'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(attrs={'type': 'password', 'class': 'input__field',
                                                                 'name': 'auth_pass',
                                                                 'placeholder': 'GoodPassword'}))
    remember_me = forms.BooleanField(label='Запомнить меня', required=False,
                                     widget=forms.PasswordInput(attrs={'type': "checkbox", 'class': "remember_checkbox",
                                                                       'id': "remember", 'name': "drone",
                                                                       'value': "huey"}))


class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email", "type": "e-mail", "class": "input__field",
                                       "name": "auth_mail",
                                       "placeholder": "kolhozniy@gmail.com", "id": "id_username"}),

    )
