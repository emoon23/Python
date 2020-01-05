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
#bot token
TOKEN = 'NjQ5MDY1MzgyNDQ3MTUzMTYz.XeG5VA.y9ayPIETTwI5j0mQE6yDJHT4xqM'
GUILD = os.getenv('DISCORD_GUILD')
BOT_PREFIX = ("!", "?")

client = discord.Client()

#client = Bot(command_prefix=BOT_PREFIX)

bot = commands.Bot(command_prefix="!")


#weather API key
owm = pyowm.OWM('bd6f22c9cb30e1ed8cd6966dcecb804f')

####################################


#Interactive commands with Valk
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
    elif message.content.startswith('fuck you'):
        await message.channel.send('You are lucky I am only a bot that has limited responses..')
    elif message.content.startswith('hi'):
        await message.channel.send('Hello, Human...')
    elif message.content.startswith('Happy Birthday'):
        await message.channel.send('Happy Birthday')
    elif message.content.startswith('happy birthday'):
        await message.channel.send('happy birthday')


#testing eight ball random
    elif message.content.startswith('!8ball'):
        possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
        ]
        await message.channel.send(random.choice(possible_responses))

#Weather of Chicago, Toronto, Los Angeles, & Denver
#@client.command(help='Gets the weather for Chicago, Toronto, Los Angeles, Denver, Rockford, & Mundelein')

    elif message.content.startswith('!weatherchicago'):
        chi = owm.weather_at_place('Chicago, US')
        weather = chi.get_weather()
        temperature = weather.get_temperature(unit='fahrenheit')['temp']
        temperature1 = weather.get_temperature(unit='celsius')['temp']
        sun_rise = weather.get_sunrise_time(timeformat='iso')
        sun_set = weather.get_sunset_time(timeformat='iso')
        await message.channel.send('The temperature is ' + str(temperature) + ' degrees Fahrenheit in ' + 'Chicago, US')
        await message.channel.send('The temperature is ' + str(temperature1) + ' degrees Celsius in ' + 'Chicago, US')
        #await message.channel.send("Sun rise at " + str(sun_rise))
        #await message.channel.send("Sun set at " + str(sun_set))

    elif message.content.startswith('!weathertoronto'):
        tor = owm.weather_at_place('Toronto, CA')
        weather = tor.get_weather()
        temperature = weather.get_temperature(unit='fahrenheit')['temp']
        temperature1 = weather.get_temperature(unit='celsius')['temp']
        sun_rise = weather.get_sunrise_time(timeformat='iso')
        sun_set = weather.get_sunset_time(timeformat='iso')
        await message.channel.send('The temperature is ' + str(temperature) + ' degrees Fahrenheit in ' + 'Toronto, CA')
        await message.channel.send('The temperature is ' + str(temperature1) + ' degrees Celsius in ' + 'Toronto, CA')
        #await message.channel.send("Sun rise at " + str(sun_rise))
        #await message.channel.send("Sun set at " + str(sun_set))

    elif message.content.startswith('!weatherla'):
        la = owm.weather_at_place('Los Angeles, US')
        weather = la.get_weather()
        temperature = weather.get_temperature(unit='fahrenheit')['temp']
        temperature1 = weather.get_temperature(unit='celsius')['temp']
        sun_rise = weather.get_sunrise_time(timeformat='iso')
        sun_set = weather.get_sunset_time(timeformat='iso')
        await message.channel.send('The temperature is ' + str(temperature) + ' degrees Fahrenheit in ' + 'Los Angeles, US')
        await message.channel.send('The temperature is ' + str(temperature1) + ' degrees Celsius in ' + 'Los Angeles, US')
        #await message.channel.send("Sun rise at " + str(sun_rise))
        #await message.channel.send("Sun set at " + str(sun_set))

    elif message.content.startswith('!weatherden'):
        den = owm.weather_at_place('Denver, US')
        weather = den.get_weather()
        temperature = weather.get_temperature(unit='fahrenheit')['temp']
        temperature1 = weather.get_temperature(unit='celsius')['temp']
        sun_rise = weather.get_sunrise_time(timeformat='iso')
        sun_set = weather.get_sunset_time(timeformat='iso')
        await message.channel.send('The temperature is ' + str(temperature) + ' degrees Fahrenheit in ' + 'Denver, US')
        await message.channel.send('The temperature is ' + str(temperature1) + ' degrees Celsius in ' + 'Denver, US')
        #await message.channel.send("Sun rise at " + str(sun_rise))
        #await message.channel.send("Sun set at " + str(sun_set))

    elif message.content.startswith('!weatherrock'):
        rock = owm.weather_at_place('Rockford, US')
        weather = rock.get_weather()
        temperature = weather.get_temperature(unit='fahrenheit')['temp']
        temperature1 = weather.get_temperature(unit='celsius')['temp']
        sun_set = weather.get_sunset_time(timeformat='iso')
        sun_set = weather.get_sunset_time(timeformat='iso')
        await message.channel.send('The temperature is ' + str(temperature) + ' degrees Fahrenheit in ' + 'Rockford, US')
        await message.channel.send('The temperature is ' + str(temperature1) + ' degrees Celsius in ' + 'Rockford, US')
        #await message.channel.send("Sun rise at " + str(sun_rise))
        #await message.channel.send("Sun set at " + str(sun_set))

    elif message.content.startswith('!weathermund'):
        mund = owm.weather_at_place('Mundelein, US')
        weather = mund.get_weather()
        temperature = weather.get_temperature(unit='fahrenheit')['temp']
        temperature1 = weather.get_temperature(unit='celsius')['temp']
        sun_set = weather.get_sunset_time(timeformat='iso')
        sun_set = weather.get_sunset_time(timeformat='iso')
        await message.channel.send('The temperature is ' + str(temperature) + ' degrees Fahrenheit in ' + 'Mundelein, US')
        await message.channel.send('The temperature is ' + str(temperature1) + ' degrees Celsius in ' + 'Mundelein, US')
        #await message.channel.send("Sun rise at " + str(sun_rise))
        #await message.channel.send("Sun set at " + str(sun_set))

    elif message.content =='raise-exception':
        raise discord.DiscordException

@bot.command(name='create-channel')
@commands.has_role('admin')
async def create_channel(ctx, channel_name='Shambo Dungeon'):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

#roll a dice
@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))



#print users connected to a server in the console
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#print name of user connected to server
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


#Welcoming new members to a discord server
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

client.run(TOKEN)
bot.run(TOKEN)
