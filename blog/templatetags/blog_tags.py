from django import template
from blog.MiladiToShamsi import shamsiDate
from datetime import datetime
from django.contrib.humanize.templatetags.humanize import intcomma

register = template.Library()

def get_day(inp_day, inp_month):
    d, m = inp_day, inp_month

    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['دوشنبه', 'سه شنبه', 'چهارشنبه', 'پنچ شنبه', 'جمعه', 'شنبه', 'یکشنبه']

    sumOfMonths = 0
    for i in range(m - 1):
        sumOfMonths += month[i]

    result = sumOfMonths + d - 1
    return days[result % 7]


@register.filter()
def shamsidate(d):
    month_dict = {1: 'فروردین', 2: 'اردیبهشت', 3: 'خرداد', 4: 'تیر', 5: 'مرداد',
                  6: 'شهریور', 7: 'مهر', 8: 'آبان', 9: 'آذر', 10: 'دی',
                  11: 'بهمن', 12: 'اسفند'}

    day = int(d.strftime("%d"))
    month = int(d.strftime("%m"))
    year = int(d.strftime("%Y"))

    shamsi = shamsiDate(year, month, day)
    today = get_day(shamsi[2], shamsi[1])
    str_shamsi = f'{today} {shamsi[2]} {month_dict[shamsi[1]]} {shamsi[0]}'

    return str_shamsi


@register.filter()
def currency(price):
    int_price = int(price)
    return '{:,}'.format(int_price)
