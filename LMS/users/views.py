from django.shortcuts import render
from django.views.generic import CreateView
from .forms import RegisterForm
from django.urls import reverse_lazy


# Create your views here.

class Register(CreateView):
    form_class = RegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('')
