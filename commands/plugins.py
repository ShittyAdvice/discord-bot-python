import discord
from discord.ext import commands

class Plugins:
  folder = 'commands.'

  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.is_owner()
  async def load(self, ctx, extension):
    try:
      self.client.load_extension( self.folder + extension )
      await ctx.send('Loaded plugin {}'.format(extension))
    except Exception as error:
      await ctx.send('Error loading plugin')
      print('Error loading plugin {}. {}'.format(extension, error))

  @commands.command()
  @commands.is_owner()
  async def unload(self, ctx, extension):
    try:
      self.client.unload_extension(self.folder + extension)
      await ctx.send('Unloaded plugin {}'.format(extension))
    except Exception as error:
      await ctx.send('Error unloading plugin')
      print('Error unloading plugin {}. {}'.format(extension, error))

  @commands.command()
  @commands.is_owner()
  async def reload(self, ctx, extension):
    try:
      self.client.unload_extension(self.folder + extension)
      self.client.load_extension( self.folder + extension )
      await ctx.send('Reloaded plugin {}'.format(extension))
    except Exception as error:
      await ctx.send('Error reloading plugin')
      print('Error reloading plugin {}. {}'.format(extension, error))

def setup(client):
  client.add_cog(Plugins(client))