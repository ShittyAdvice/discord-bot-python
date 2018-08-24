import discord, random
from discord.ext import commands

class Other:
  def __init__(self, client):
    self.client = client
    self.client.remove_command('help')

  @commands.command()
  async def invite(self, ctx):
      """Generates and sends an invite link to add this bot to the server."""
      url = discord.utils.oauth_url(self.client.user.id)
      await ctx.author.send(f":hugging: I'm always happy to make new friends! Invite me to your server with this link\n{url}")

  @commands.command()
  async def help(self, ctx):
      lyric = random.choice([
          "Mars ain't the kind of place to raise your kids",
          "Mars ain't the kind of place to raise your kids\nIn fact it's cold as hell",
          "It's lonely out in space",
          "Oh no no no I'm a rocket ~~man~~ bot",
          "On such a timeless flight",
          "I'm not the man they think I am at home"
      ])
      embed = discord.Embed(title='Rocket Bot', description=lyric, color=0x2196F3)

      embed.add_field(name='!youtube {id|url}', value='Adds a youtube video to the queue. This will automatically connect to the authors channel and start playing', inline=False)
      embed.add_field(name='!skip', value='Skips the current song', inline=False)
      embed.add_field(name='!pause', value='Pause the audio player', inline=False)
      embed.add_field(name='!resume', value='Resume the audio player', inline=False)
      embed.add_field(name='!stop', value='Stops the audio player completely and empties the queue', inline=False)
      embed.add_field(name='!clear {x}', value='Clears the last {x} amount of messages.\nThe default and maximum value is 100 messages.\nThe bot is required to have the `Manage Messages` role for this to work.', inline=False)
      embed.add_field(name='!help', value='Shows this help message', inline=False)

      await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Other(client))