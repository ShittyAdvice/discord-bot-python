from rocketbot.client import client, discord

class MusicPlayer:
  def __init__(self, voiceClient: discord.VoiceClient):
    self.queue = []
    self.voiceClient = voiceClient

  def play(self):
    if self.voiceClient.is_playing() or not self.queue:
      return

    try:
      self.voiceClient.play(discord.FFmpegPCMAudio(self.queue.pop(0)), after=self.onPlaybackFinished)
      self.voiceClient.source.volume = 1
    except Exception as e:
      print('An error occured in MusicPlayer.play()', e)

  def stop(self):
    self.queue = []
    self.onPlaybackFinished(error=None)

  def skip(self):
    self.voiceClient.stop()

  def resume(self):
    if self.voiceClient.is_paused():
      self.voiceClient.resume()

  def pause(self):
    if self.voiceClient.is_playing():
      self.voiceClient.pause()

  def enqueue(self, item):
    self.queue.append(item)

  def onPlaybackFinished(self, error):
    if error:
      print('An error occured in MusicPlayer.onPlaybackFinished()', error)

    if not self.queue:
      client.loop.create_task(self.voiceClient.disconnect())
    else:
      self.play()
