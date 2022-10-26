import datetime
import re
from .models import Lecture
from calendar import HTMLCalendar
import locale

locale.setlocale(locale.LC_ALL, 'ru_Ru')


def calendar(m):
    now = datetime.datetime.now()
    month = now.month + m
    if month > 12:
        month -= 12
    cal = HTMLCalendar().formatmonth(
        now.year,
        month
    )
    lectures = Lecture.objects.filter(date__month=now.month + m)
    cal = cal.split()
    cal[0] += ' id=table' + str(m)
    for lecture in lectures:
        for i in range(len(cal)):
            print(cal[i])
            day = re.findall(r'\d+', cal[i])
            if day:
                if day[0] == str(lecture.date.day) and 'href' not in cal[i]:
                    cal[i] = str(cal[i]).replace(day[0],
                                                 f'<a class=\'lecture_date\' href=\'course/lectures/{day[0]}/\'>{day[0]}</a>')
                    cal[i-1] += " class=lecture_select"

    cal = ' '.join(cal)
    return cal
