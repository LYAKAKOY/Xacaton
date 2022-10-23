from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from .forms import RegisterForm, AuntificationUserForm
from django.urls import reverse_lazy


# Create your views here.

class Registration(CreateView):
    form_class = RegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('')


class Auntification(LoginView):
    form_class = AuntificationUserForm
    template_name = 'users/login.html'
