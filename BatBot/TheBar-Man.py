################IMPORTS####################
import os
import discord
import random
import requests, json
import pyowm
##########################################


####################################
from dotenv import load_dotenv
from discord.ext.commands import Bot
from discord.ext import commands

load_dotenv()
TOKEN = 'NzMyMzY1MTY4MjQzMzc2MjY5.Xwzm7w.LLaiImiieoClXhTarr8KxZoMqaQ'
GUILD = os.getenv('DISCORD_GUILD')
BOT_PREFIX = ("!", "?")

client = discord.Client()

bot = commands.Bot(command_prefix="!")



####################################
#Interactive commands with Valk

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send('Hello, human')
    elif message.content.startswith('hello'):
        msg = 'Hey hey {0.author.mention}'.format(message)
        await message.channel.send('Hey Hey!')




    #Testing bar man commands
    if message.content.startswith('drink'):
        # Poisons
        possible_responses = ['Vodka','Tequila', 'Bourbon','Scotch','Whiskey','Gin', 'Rum', 'Malort', 'Hennessey' ]
        await message.channel.send('Take a shot of ' + random.choice(possible_responses))
        # responses

    #When someone says 'no'
    if message.content.startswith('no'):
        possible_responses2 = ['...you coward..fooking drink!', 'why not friend?', 'I thought we were friends']
        await message.channel.send(random.choice(possible_responses2))



#print users connected to a server in the console
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


#Welcoming new members to a discord server
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to the Discord server!')



client.run(TOKEN)
bot.run(TOKEN)
