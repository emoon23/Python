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

#bot = commands.Bot(command_prefix="!")

#base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

#Request user input first
#user = input('Would like to know what the weather is today? ')

#Conditional Statement
#if user == 'Yes' or user == 'yes':

city_Name = input('Please enter the name of a city in the US: ')

complete_url = base_url + "appid=" + api_key + "&q=" + city_Name

responses = requests.get(complete_url)

x = responses.json()

#x contains a list of nested disctionaries

    #Check if api key is equal to "404", means city is found otherwise,
    #City is not found
if x['cod'] != "404":

        #Store the value of "main"
        #key in the variable y
        y = x["main"]

        #store the value corresponding
        #to the "temp" key of y
        current_temp = y["temp"]

        #store the value corresponding
        #to the "pressure" key of y
        current_press = y["pressure"]

        #store the value humidity key in y
        current_humid = y["humidity"]

        #store the value of weather
        #key in variable z
        z = x["weather"]

        #Store the value corresponding
        #To the weather description key at
        #the 0th index of z
        weather_descript = z[0]["description"]

        print(" Temperature (in kelvin unit) = " +
                    str(current_temp) +
                "\n atmospheric pressure (in hPa unit) = " +
                    str(current_press) +
                "\n humidity (in precentage) = " +
                    str(current_humid) +
                "\n description = " +
                    str(weather_descript))
else:
        print(" City not found ")
