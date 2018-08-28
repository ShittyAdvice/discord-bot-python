from rocketbot.client import client, discord
from rocketbot.reactionlistener import ReactionListener

class MusicPlayerMessage:
  def __init__(self, player, channel):
    self.message = None
    self.player = player
    self.channel = channel

    self.create()

  def create(self):
    async def send():
      self.message = await self.channel.send('**Music Player**', embed=self.embed())
      self.reactionListener = ReactionListener(self.message)
      self.reactionListener.onReactionReceived('⏯', self.player.playOrPause)
      self.reactionListener.onReactionReceived('⏭', lambda r, u: self.player.skip())
      self.reactionListener.onReactionReceived('🔉', lambda r, u: self.player.setVolume(self.player.volume - 0.05))
      self.reactionListener.onReactionReceived('🔊', lambda r, u: self.player.setVolume(self.player.volume + 0.05))
      self.reactionListener.onReactionReceived('🔇', lambda r, u: self.player.mute())
      self.reactionListener.onReactionReceived('🔈', lambda r, u: self.player.unmute())

    client.loop.create_task(send())


  def update(self):
    if not self.message:
      client.loop.call_later(1, self.update)
      return

    async def edit():
      await self.message.edit(content='**Music Player**', embed=self.embed())

    client.loop.create_task(edit())

  def delete(self):
    self.message.delete()
    self.message = None

  def embed(self):
    embed = discord.Embed(colour=0x98FB98)
    embed.add_field(name='Now Playing', value=self.nowPlaying())
    embed.add_field(name='Volume', value=self.volume())
    embed.add_field(name='Duration', value=self.duration())
    embed.add_field(name='Next Song', value=self.nextSong())
    embed.add_field(name='Queue Size', value=str(len(self.player.queue)))
    return embed

  def volume(self):
    volume = f'{round(self.player.volume * 100)}%'
    if self.player.isMuted:
      volume += ' (muted)'
    return volume

  def duration(self):
    if self.player.currentSong:
      return self.player.currentSong.duration
    else:
      return '-'

  def nextSong(self):
    if self.player.queue:
      return self.player.queue[0].name
    else:
      return 'None'

  def nowPlaying(self):
    if self.player.currentSong:
      return self.player.currentSong.name
    elif self.player.isPaused():
      return 'Paused'
    else:
      return 'Stopped'
