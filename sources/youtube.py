import datetime

import gdata.youtube.service
import atom

#TODO No timezone - is time in UTC?
def atom_datetime(atom_date):
    return datetime.datetime.strptime(atom_date.text, '%Y-%m-%dT%H:%M:%S.%fZ')

class YoutubeVideo(object):
    
    def __init__(self, entry):
        self.entry = entry

    # def __getattr__(self, attr):
    #     value = getattr(self.entry, attr) 
    #     if isinstance(value, atom.Date):
    #         return datetime.datetime.strptime(value.text, '%Y-%m-%dT%H:%M:%S.%fZ')
    #     return value.text

    @property
    def title(self):
        return self.entry.title.text

    @property
    def thumbnails(self):
        return entry.media.thumbnails

    def __repr__(self):
        return "YoutubeVideo: '%s'" % self.title

def list_videos(username):
    yt_service = gdata.youtube.service.YouTubeService()
    feed = yt_service.GetYouTubeVideoFeed('https://gdata.youtube.com/feeds/api/users/%s/uploads' % username)
    return [YoutubeVideo(entry) for entry in feed.entry]
