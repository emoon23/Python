import os
import requests, json
import pyowm



from dotenv import load_dotenv
from discord.ext.commands import Bot
from discord.ext import commands

load_dotenv()

"""
Discord Commands
"""
#TOKEN =
#BOT_PREFIX = ("!", "?")

#client = discord.Client()

#Open Weather Map API
api_key = 'da86b8b590aa4e97abe168bac1d99a29'

bot = commands.Bot(command_prefix="!")

#base_url variable to store url
base_url = "http://maps.openweathermap.org/maps/2.0/weather.TA2/{z}/{x}/{y}?date=1527811200&opacity=0.9&fill_bound=true&appid={api_key}"

#Request user input first
user = input('Would like to know what the weather is today? ')

#Conditional Statement
if user == 'Yes' or user == 'yes':

    city_Name = input('Please enter the name of a city in the US: ')

    complete_url = base_url + "appid=" + api_key + "&q=" + city_Name

    responses = requests.get(complete_url)

    x = responses.json()

    #x contains a list of nested disctionaries

    #Check if api key is equal to "404", means city is found otherwise,
    #City is not found
    if x['cod'] != "404":
