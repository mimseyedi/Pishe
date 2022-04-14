from django import template
from blog.MiladiToShamsi import shamsiDate
from datetime import datetime

register = template.Library()


@register.filter()
def shamsidate(d):
    day = int(d.strftime("%d"))
    month = int(d.strftime("%m"))
    year = int(d.strftime("%Y"))

    shamsi = shamsiDate(year, month, day)
    str_shamsi = f'{shamsi[0]}/{shamsi[1]}/{shamsi[2]}'

    return str_shamsi
