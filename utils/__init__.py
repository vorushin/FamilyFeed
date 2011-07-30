from django.contrib.sites.models import Site

def log_exception(text, **kwargs):
    kwargs['exc_info'] = sys.exc_info()
    logging.error(text, **kwargs)

def absolute_uri(location, request=None):
    return '%s://%s%s' % (
        'https' if request and request.is_secure() else 'http',
        Site.objects.get_current().domain,
        location)
