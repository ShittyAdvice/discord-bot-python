from discord.ext import commands
from classes.youtube import Youtube
from classes.musicplayer import MusicPlayer

class Audio:
  def __init__(self, client):
    self.client = client
    self.players = {}

  def getPlayer(self, guildId):
    return self.players.get(guildId)

  @commands.command()
  async def pause(self, ctx):
    player = self.getPlayer(ctx.message.guild.id)

    if player:
      player.pause()

  @commands.command()
  async def resume(self, ctx):
    player = self.getPlayer(ctx.message.guild.id)

    if player:
      player.resume()

  @commands.command()
  async def stop(self, ctx):
    player = self.getPlayer(ctx.message.guild.id)

    if player:
      player.skip()

  @commands.command()
  async def skip(self, ctx):
    player = self.getPlayer(ctx.message.guild.id)

    if player:
      player.skip()

  @commands.command()
  async def youtube(self, ctx, url):
    guild = ctx.message.guild
    if not ctx.author.voice:
      await ctx.send('You are not connected to a voice channel')
      return

    player = self.players.get(guild.id)

    if not player or not player.voiceClient.is_connected():
      voiceClient = await ctx.author.voice.channel.connect()
      player = self.players[guild.id] = MusicPlayer(voiceClient)

    player.enqueue(Youtube.getMP3(url))
    player.play()

def setup(client):
  client.add_cog(Audio(client))