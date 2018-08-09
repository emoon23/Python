# -*- coding: utf-8 -*-
"""
Created on Mon May 21 10:43:24 2018

@author: Edward
"""

# A python program of a pie chart for my day to day life....


import matplotlib.pyplot as plt

#Data
labels = 'Workout', 'Miscellaneous', 'Social', 'Work'
sizes = [50, 70, 180, 480] #Hours spent throughout the week
colors = ['gold', 'lightskyblue', 'lightcoral', 'yellowgreen']
explode = (0.1, 0 , 0 ,0)

#plot  the pie graph
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show() #Display the great pie!