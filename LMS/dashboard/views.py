from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import services
from .models import Course, Lecture


class CoursesView(LoginRequiredMixin, ListView):
    model = Course
    template_name = "dashboard/dashboard.html"
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['calendar1'] = services.calendar(-5)
        context['calendar2'] = services.calendar(-4)
        context['calendar3'] = services.calendar(-3)
        context['calendar4'] = services.calendar(-2)
        context['calendar5'] = services.calendar(-1)
        context['calendar6'] = services.calendar(0)
        context['calendar7'] = services.calendar(1)
        context['calendar8'] = services.calendar(2)
        context['calendar9'] = services.calendar(3)
        context['calendar10'] = services.calendar(4)
        context['calendar11'] = services.calendar(5)
        return context


class AllCoursesView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'dashboard/allcourses.html'
    context_object_name = 'courses'


class CourseView(LoginRequiredMixin, DetailView):
    model = Course
    template_name = 'dashboard/course.html'
    slug_url_kwarg = 'slug_course'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['course'].name_course
        context['lectures'] = Lecture.objects.filter(course__slug=context['course'].slug)
        context['teachers'] = context['course'].teacher.all()
        print(context['teachers'])
        return context


class LectureView(LoginRequiredMixin, DetailView):
    model = Lecture
    template_name = 'dashboard/lecture.html'
    slug_url_kwarg = 'slug_lecture'
    context_object_name = 'lecture'


@login_required
def lectures_day(request, day_lecture):
    lectures = Lecture.objects.filter(date__day=day_lecture)
    data = {
        'lectures': lectures
    }
    return render(request, 'dashboard/lectures_day.html', data)


@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')
