from rocketbot.client import client

class ReactionListener:
  def __init__(self, message):
    self.callbacks = {}
    self.message = message
    self.isListening = False

  def check(self, reaction, user):
    print(reaction.emoji)
    return not user.bot and reaction.emoji in self.callbacks

  async def waitFor(self):
    reaction, user = await client.wait_for('reaction_add', check=self.check)

    self.callbacks[reaction.emoji](reaction, user)
    try:
      await self.message.remove_reaction(reaction, user)
    except Exception as e:
      print('An error occured removing reaction. Make sure bot has permissions\n', e)

    if not self.callbacks:
      self.isListening = False
    else:
      await self.waitFor()

  def onReactionReceived(self, emoji, callback, react=True):
    """ Add a reaction command """
    self.callbacks[emoji] = callback

    if react:
      client.loop.create_task(self.message.add_reaction(emoji))

    if not self.isListening:
      self.isListening = True
      client.loop.create_task(self.waitFor())