import discord
import random

client = discord.Client()

prefix = '%'

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix+'help'):
        await message.channel.send('```Commands:\nhelp\nroll X```')
    elif message.content.startswith(prefix+'roll'):
        n = roll(message)
        await message.channel.send("Rolled: " + str(n))

def roll(message) -> int:
    num = int(message.content.split(' ')[1])
    return random.randint(0, num)

client.run('Token here')
