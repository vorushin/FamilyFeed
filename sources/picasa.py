import gdata.photos.service

# http://code.google.com/apis/picasaweb/docs/1.0/developers_guide_python.html#GettingStarted

def auth_url(next):
    gd_client = gdata.photos.service.PhotosService()
    scope = 'https://picasaweb.google.com/data/'
    secure = False
    session = True
    gd_client = gdata.photos.service.PhotosService()
    return gd_client.GenerateAuthSubURL(next, scope, secure, session);

def list_albums(login, token):
    return gd_client.GetUserFeed(user=login)
