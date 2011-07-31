import datetime

import gdata.youtube.service
import atom

#TODO No timezone - is time in UTC?
def atom_datetime(atom_date):
    return datetime.datetime.strptime(atom_date.text, '%Y-%m-%dT%H:%M:%S.%fZ')

class YoutubeVideo(object):
    
    def __init__(self, entry):
        self.title = entry.title.text.decode('utf-8')
        self.published = atom_datetime(entry.published)
        self.thumbnails = entry.media.thumbnail
        self.url = entry.media.content[0].url

    def json(self):
        return self.__dict__

    def __repr__(self):
        return "YoutubeVideo: '%s'" % self.title

def list_videos(username):
    yt_service = gdata.youtube.service.YouTubeService()
    feed = yt_service.GetYouTubeVideoFeed('https://gdata.youtube.com/feeds/api/users/%s/uploads' % username)
    return [YoutubeVideo(entry) for entry in feed.entry]
