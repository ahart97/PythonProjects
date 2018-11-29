from bs4 import BeautifulSoup
import requests
import pandas as pd
from tkinter import *


root = Tk()

days = []
temp = []
url = 'https://weather.gc.ca/city/pages/on-82_metric_e.html'

locations = [('Kitchener','https://weather.gc.ca/city/pages/on-82_metric_e.html'),
('Toronto','https://weather.gc.ca/city/pages/on-143_metric_e.html')]

def get_day_info(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    seven_day = soup.find(class_='div-table')
    return seven_day

def get_temp(seven_day):
    week_temp = seven_day.find_all(class_='high wxo-metric-hide')
    for temps in week_temp:
        temp.append(temps.get_text())
    temp[0] = '\n' + temp[0]
    return temp

def get_days(seven_day):
    week_days = seven_day.find_all(class_='div-row div-row1 div-row-head')
    for day in week_days:
        days.append(day.get_text())
    return days

def update(url):
    temp = get_temp(get_day_info(url))
    days = get_days(get_day_info(url))
    for i in range (7):
        x = Label(root, text = days[i] + ' ' + temp[i])
        x.pack(side = LEFT)

for places, html in locations:
    b = Radiobutton(root,text = places, variable = url, value = html,
    command = lambda : update(url))
    b.pack(side = LEFT)

root.mainloop()
