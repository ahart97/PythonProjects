from bs4 import BeautifulSoup
import requests
from tkinter import *

root = Tk()


def get_future_forcast(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    future_forcast = soup.find(class_='looking-ahead')
    return future_forcast

def get_temp(future_forcast):
    temps = future_forcast.find_all(class_='today-daypart-temp')
    all_temps = ''
    for temp in temps:
        all_temps = all_temps + temp.get_text()
    return all_temps

cities_html = {'Toronto' : 'https://weather.com/en-CA/weather/today/l/62e0efebee1ac0e8fa9b21fd17d57a6a0001753ab6be8a4874bb78bbb52eda02',
'Waterloo' : 'https://weather.com/en-CA/weather/today/l/CAXX0531:1:CA'}

TO_temp = get_temp(get_future_forcast(cities_html['Toronto']))
UW_temp = get_temp(get_future_forcast(cities_html['Waterloo']))

cities = {'Toronto': TO_temp, 'Waterloo' : UW_temp}

var = StringVar()

class Display:
    def __init__(self,master):

        '''Creates frame for the weather information'''

        frame = Frame(master, width = 200, height = 500)
        frame.pack(side = RIGHT)

        '''Creates a label to display temp'''

        self.temp = Label(frame, textvariable = var)
        self.temp.pack()

class Selection:
    def __init__(self,master):

        '''Creates frame for selection of city'''

        frame = Frame(master, width = 100, height = 500,padx = 10, pady = 10)
        frame.pack(side = LEFT)

        '''Creating all the Radiobutton selections'''

        for place, temp in cities.items():
            self.select = Radiobutton(frame, text = place, variable = var, value = temp,
            indicatoron = 0, width = 25)
            self.select.pack()

Info = Selection(root)
Weather = Display(root)

root.mainloop()
