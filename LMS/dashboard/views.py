import datetime
import re

from django.views.generic import ListView, DetailView
from .models import Course, Lecture
from calendar import HTMLCalendar


class CoursesView(ListView):
    paginate_by = 3
    model = Course
    template_name = "dashboard/main_page.html"
    context_object_name = 'courses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.datetime.now()
        context['calendar'] = HTMLCalendar().formatmonth(
            now.year,
            now.month
        )
        lectures = Lecture.objects.all()
        cal = context.get('calendar').split()
        for lecture in lectures:
            for i in range(len(cal)):
                day = re.findall(r'\d+', cal[i])
                if day:
                    if day[0] == str(lecture.date.day):
                        cal[i] = str(cal[i]).replace(day[0], f'<a class=\'lecture_date\' href=\'course/lecture/{lecture.slug}/\'>{day[0]}</a>')

        context['calendar'] = ' '.join(cal)
        return context


class CourseView(DetailView):
    model = Course
    template_name = 'dashboard/course.html'
    slug_url_kwarg = 'slug_course'
    context_object_name = 'course'


class LectureView(DetailView):
    model = Lecture
    template_name = 'dashboard/lecture.html'
    slug_url_kwarg = 'slug_lecture'
    context_object_name = 'lecture'
