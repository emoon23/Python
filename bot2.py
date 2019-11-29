import os
import discord
import random

from dotenv import load_dotenv

load_dotenv()
TOKEN = 'NjQ5MDY1MzgyNDQ3MTUzMTYz.Xd73Aw.GM3nfS7Yqaf9mut7lGgrRwz9_LE'
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send('Hello, Human...')
        #await client.send_message(message.channel, msg)
    elif message.content.startswith('hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send('Hello, Human...')
    elif message.content.startswith('Valk'):
        await message.channel.send('You rang?')
    elif message.content.startswith('valk'):
        await message.channel.send("That's me")
    elif message.content.startswith('bitch'):
        await message.channel.send('You dare speak to me like that?')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break


    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f 'Hi {member.name}, welcome to my Discord server!'
    )

client.run(TOKEN)

"""
BOT_PREFIX = ("?", "!")
TOKEN = "NjQ5MDY1MzgyNDQ3MTUzMTYz.Xd73Aw.GM3nfS7Yqaf9mut7lGgrRwz9_LE"

client = Bot(command_prefix=BOT_PREFIX)

@client.command()
async def eight_ball():
    possible_responses = [
    'That is a resounding no',
    'It is not looking likely',
    'Too hard to tell',
    'It is quite possible',
    'Definitely',

    ]
    await client.say(random.choice(possible_responses))



client.run(TOKEN)
"""
