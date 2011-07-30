from __future__ import absolute_import

import base64
from cgi import parse_qs
from functools import wraps
import hashlib
import hmac
from urllib import urlopen, urlencode

from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponseBadRequest
import facebook

from utils import log_exception, absolute_uri

class FacebookError(Exception):
    pass


class BadRequestError(Exception):
    pass


# def base64_url_decode(inp):
#     padding_factor = (4 - len(inp) % 4) % 4
#     inp += '=' * padding_factor
#     return base64.b64decode(
#         unicode(inp).translate(dict(zip(map(ord, u'-_'), u'+/'))))


# source - http://sunilarora.org/parsing-signedrequest-parameter-in-python-bas
# def parse_signed_request(signed_request, secret):
#     encoded_sig, payload = signed_request.split('.', 2)

#     sig = base64_url_decode(encoded_sig)
#     data = json.loads(base64_url_decode(payload))

#     if data.get('algorithm').upper() != 'HMAC-SHA256':
#         raise Exception('Unknown algorithm')

#     expected_sig = hmac.new(secret, msg=payload, digestmod=hashlib.sha256)\
#         .digest()
#     if sig != expected_sig:
#         raise Exception('Signature error')

#     return data


def request_facebook_permissions(request, permissions, redirect_url):
    params = {
        'client_id': settings.FACEBOOK_API_KEY,
        'redirect_uri': settings.FACEBOOK_REDIRECT_URL,
        'scope': ','.join(permissions),
    }
    return HttpResponseRedirect('https://graph.facebook.com/oauth/authorize?' +
                                urlencode(params))

def get_facebook_access_token(request):
    if 'error' in request.GET:
        log_exception(
            'Error in get_facebook_access_token',
            extra={'error': request.GET.get('error'),
                   'error_reason': request.GET.get('error_reason'),
                   'error_description': request.GET.get('error_description')})
        raise FacebookError(request.GET['error'])

    if not 'code' in request.GET:
        raise BadRequestError

    code = request.GET.get('code', '')
    if not code:
        raise Exception

    params = {
        'client_id': settings.FACEBOOK_API_KEY,
        'client_secret': settings.FACEBOOK_SECRET_KEY,
        'redirect_uri': settings.FACEBOOK_REDIRECT_URL,,
        # 'redirect_uri': absolute_uri(request.path, request),
        'code': code,
    }
    response = urlopen('https://graph.facebook.com/oauth/access_token?'
                       + urlencode(params)).read()
    if response.find(error) != -1:
        raise FacebookError(response)
    return parse_qs(response)['access_token'][-1]


def facebook_callback(func):
    @wraps(func)
    def callback_view(request, *args, **kwargs):
        try:
            access_token = get_facebook_access_token(request)
        except FacebookError as e:
            messages.error(request, 'Facebook authorization error: %s' % e)
            access_token = None
        except BadRequestError as e:
            return HttpResponseBadRequest(e)
        return func(request, access_token, *args, **kwargs)
    return callback_view
