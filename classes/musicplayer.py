import time
from rocketbot.client import client, discord
from classes.musicplayermessage import MusicPlayerMessage

class MusicPlayer:
  def __init__(self, textChannel: discord.TextChannel, voiceClient: discord.VoiceClient = None):
    self.queue = []
    self.volume = 0.5
    self.isMuted = False
    self.currentSong = None
    self.voiceClient = voiceClient
    self.message = MusicPlayerMessage(self, textChannel)

  async def connect(self, channel):
    if self.voiceClient and self.voiceClient.is_connected():
      return
    self.voiceClient = await channel.connect()
    self.message.update()

  async def disconnect(self):
    await self.message.delete()
    await self.voiceClient.disconnect()
    self.voiceClient = None

  def isPaused(self):
    return self.voiceClient and self.voiceClient.is_paused()

  def mute(self):
    self.isMuted = True
    self.voiceClient.source.volume = 0
    self.message.update()

  def unmute(self):
    self.isMuted = False
    self.setVolume(self.volume)

  def play(self):
    if not self.voiceClient or self.voiceClient.is_playing() or (not self.queue and not self.currentSong):
      return
    
    if self.isPaused():
      return self.voiceClient.resume()

    try:
      self.currentSong = self.queue.pop(0)
      source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(self.currentSong.path), self.volume)
      self.voiceClient.play(source, after=self.onPlaybackFinished)
      self.message.update()
    except Exception as e:
      print('An error occured in MusicPlayer.play()', e)

    
  def stop(self):
    self.queue = []
    self.onPlaybackFinished(error=None)

  def skip(self):
    self.voiceClient.stop()
    self.message.update()

  def resume(self):
    self.voiceClient.resume()
    self.message.update()

  def pause(self):
    self.voiceClient.pause()
    self.message.update()

  def playOrPause(self, reaction, user):
    if not self.voiceClient:
      if not user.voice:
        client.loop.create_task(self.message.channel.send(f'{user.mention} You are not connected to a voice channel'))
      else:
        client.loop.create_task(self.connect(user.voice.channel))
    elif self.voiceClient.is_playing():
      self.pause()
    else:
      self.play()

  def enqueue(self, item):
    self.queue.append(item)
    self.message.update()

  def setVolume(self, volume):
    if volume >=  1.0:
      volume = 1
    elif volume <= 0.0:
      volume = 0

    self.volume = volume

    if self.voiceClient and self.voiceClient.source and not self.isMuted:
      self.voiceClient.source.volume = self.volume

    self.message.update()

  def onPlaybackFinished(self, error):
    if error:
      print('An error occured in MusicPlayer.onPlaybackFinished()', error)

    if not self.queue:
      client.loop.create_task(self.disconnect())
    else:
      self.play()