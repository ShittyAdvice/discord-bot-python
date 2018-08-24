import os, discord, asyncio, random
from discord.ext import commands

client = commands.Bot(command_prefix='!')

async def status_task():
    while True:
        planet = random.choice(['Saturn', 'Jupiter', 'Earth', 'Uranus', 'Mercury', 'Mars', 'Venus', 'Neptune'])
        game = discord.Game(name='on {}'.format(planet))

        await client.change_presence(activity=game)
        await asyncio.sleep(15 * 60)

@client.event
async def on_ready():
    print(client.user.name + ' is ready for action! (UserID: ' + str(client.user.id) + ')\n')
    client.loop.create_task(status_task())
    extensions = ['commands.plugins', 'commands.audio', 'commands.other', 'commands.channel']

    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded. {}'.format(extension, error))