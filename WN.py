from bs4 import BeautifulSoup
import requests
import pandas as pd
from tkinter import *


root = Tk()

days = []
temp = []

page = requests.get('https://weather.gc.ca/city/pages/on-82_metric_e.html')
soup = BeautifulSoup(page.content, 'html.parser')

seven_day = soup.find(class_='div-table')

week_days = seven_day.find_all(class_='div-row div-row1 div-row-head')

week_temp = seven_day.find_all(class_='high wxo-metric-hide')

for temps in week_temp:
    temp.append(temps.get_text())

for day in week_days:
    days.append(day.get_text())

temp[0] = '\n' + temp[0]

for i in range (7):
    x = Label(root, text = days[i] + ' ' + temp[i]).pack()

root.mainloop()
