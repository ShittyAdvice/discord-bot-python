import youtube_dl

class Youtube:
  @staticmethod
  def getMP3(url):
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
      # print('Video ID: ' + info['id'])
      # print('Thumbnail: ' + info['thumbnail'])
      # print('Duration: ' + str(info['duration']))
      # print('URL: ' + str(info['formats'][0]['url']))
      return info['formats'][0]['url']
    return None