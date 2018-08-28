import asyncio
from discord import Embed, reaction
from discord.ext import commands
from classes.youtube import Youtube
from classes.musicplayer import MusicPlayer

class Audio:
  players = {}
  def __init__(self, client):
    self.client = client
    self.players = {}

  def getPlayer(self, ctx):
    guild = ctx.message.guild
    player = self.players.get(guild.id)

    if not player:
      self.players[guild.id] = MusicPlayer(ctx.message.channel)
    return self.players[guild.id]

  @commands.command(aliases=['q'])
  async def queue(self, ctx, videoUrl):
    player = self.getPlayer(ctx)
    song = Youtube.getSong(videoUrl)
    if song:
      player.enqueue(song)

    await ctx.message.delete()

  @commands.command(aliases=['mp'])
  async def musicplayer(self, ctx):
    player = self.getPlayer(ctx)
    # if not player:
    #   if not ctx.author.voice:
    #     return await ctx.send(f'{ctx.author.mention} please connect to a voice channel, otherwise I don\'t know what channel to launch towards')

    #   vc = await ctx.author.voice.channel.connect()
    #   player = self.players[ctx.message.guild.id] = MusicPlayer(vc)

    # await player.createControls(ctx.message.channel)

  @commands.command()
  async def pause(self, ctx):
    player = self.players.get(ctx.message.guild.id)

    if player:
      player.pause()

  @commands.command()
  async def resume(self, ctx):
    player = self.players.get(ctx.message.guild.id)

    if player:
      player.resume()

  @commands.command()
  async def stop(self, ctx):
    player = self.players.get(ctx.message.guild.id)

    if player:
      player.stop()

  @commands.command()
  async def skip(self, ctx):
    player = self.players.get(ctx.message.guild.id)

    if player:
      player.skip()

  # @commands.command()
  # async def youtube(self, ctx, url):
  #   guild = ctx.message.guild
  #   if not ctx.author.voice:
  #     await ctx.send('You are not connected to a voice channel')
  #     return

  #   player = self.players.get(guild.id)

  #   if not player or not player.is_connected():
  #     voiceClient = await ctx.author.voice.channel.connect()
  #     player = self.players[guild.id] = MusicPlayer(voiceClient)

  #   song = Youtube.getSong(url)
  #   if song:
  #     player.enqueue(song)

def setup(client):
  client.add_cog(Audio(client))