import youtube_dl
from classes.song import Song

class Youtube:
  @classmethod
  def getSong(self, url):
    info = self.getInfo(url)
    if not info:
      return None

    return Song(info['title'], info['formats'][0]['url'], info['duration'], info['thumbnail'])

  @classmethod
  def getInfo(self, url):
    def myHook(d):
      print(d['status'])
 
    opts = {
      'format': 'bestaudio/best',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
      }],
      'progress_hooks': [myHook],
    }
    with youtube_dl.YoutubeDL(opts) as ydl:
      info = ydl.extract_info(url, download=False)
      return info
    return None