from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView
from .models import Course


class CoursesView(ListView):
    model = Course
    template_name = "dashboard/main_page.html"
    context_object_name = 'courses'

