from __future__ import absolute_import

import calendar
import datetime
import logging
import sys

from django.contrib.sites.models import Site


def log_exception(text, **kwargs):
    kwargs['exc_info'] = sys.exc_info()
    logging.error(text, **kwargs)


def absolute_uri(location, request=None):
    return '%s://%s%s' % (
        'https' if request and request.is_secure() else 'http',
        Site.objects.get_current().domain,
        location)


def make_uri_title(value):
    import trans
    return value.encode('trans/slug')


def comma_split(keywords):
    if not keywords.strip():
        return []
    return [k.strip() for k in keywords.split(',')]

def make_age(birthdate):
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
