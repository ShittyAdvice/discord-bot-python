import discord
from discord.ext import commands

class Channel:
  def __init__(self, client):
    self.client = client

  @commands.command()
  @commands.is_owner()
  async def clear(self, ctx, amount: int = 100):
    try:
      channel = ctx.message.channel
      messages = []
      async for message in channel.history(limit=amount):
        messages.append(message)
      await channel.delete_messages(messages)
    except discord.errors.Forbidden:
      await ctx.send(f'{ctx.message.author.mention} I do not have the permission to manage messages :fox:')
    except Exception:
      await ctx.send('Could not delete your messages.\nReminder: You cannot delete more than 100 messages')

def setup(client):
  client.add_cog(Channel(client))