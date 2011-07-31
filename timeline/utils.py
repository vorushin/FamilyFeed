from __future__ import absolute_import

import datetime
import calendar

def age(birthdate):
    now = datetime.datetime.now()
    years = now.year - birthdate.year
    if now.month < birthdate.month or (now.month == birthdate.month and now.day < birthdate.day):
        years = years - 1
        months = 12 - birthdate.month + now.month
    else:
        months = now.month - birthdate.month
    if years >= 5:
        return '%s years' % years
    if now.day < birthdate.day:
        months -= 1
    if months == 0:
        if now.day < birthdate.day:
            last_day_of_month = calendar.monthrange(birthdate.year, birthdate.month)[1]
            days = last_day_of_month - birthdate.day + now.day
        else:
            days = now.day - birthdate.day
        return '%s days' % days
    if years < 1:
        return '%s months' % months
    return '%s years %s months' % (years, months)
    

