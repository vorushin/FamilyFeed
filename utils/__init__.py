from __future__ import absolute_import
import logging
import re
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
    # copied from django.templates.defaultfilters
    import unicodedata
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    return re.sub('[-\s]+', '-', value)
