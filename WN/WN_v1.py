from bs4 import BeautifulSoup
import requests
from tkinter import *

root = Tk()
root.title('Weather')

def get_future_forcast(url):

    '''Locatate where the forcasts are being held'''

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    future_forcast = soup.find(class_='looking-ahead')
    return future_forcast

def get_temp(future_forcast):

    '''Get the temps for the forcast'''

    temps = future_forcast.find_all(class_='today-daypart-temp')
    all_temps = []
    for temp in temps:
        all_temps.append(temp.get_text())
    return all_temps

def get_time(future_forcast):

    '''Get the date for the forcast'''

    times = future_forcast.find_all(class_='today-daypart-title')
    all_times = []
    for time in times:
        all_times.append(time.get_text())
    return all_times

def get_status(future_forcast):

    '''Get the description of the forcast'''

    status = future_forcast.find_all(class_='today-daypart-wxphrase')
    all = []
    for each in status:
        all.append(each.get_text())
    return all

def lists_to_string(city):

    '''Convert the time, temp and status to one string to display'''

    list1 = get_time(get_future_forcast(cities_html[city]))
    list2 = get_temp(get_future_forcast(cities_html[city]))
    list3 = get_status(get_future_forcast(cities_html[city]))
    new_list = []
    for i in range(len(list1)):
        temp_list = [list1[i],list2[i],list3[i]]
        new_list.append(' '.join(temp_list))
    return '\n'.join(new_list)

cities_html = {'Toronto' : 'https://weather.com/en-CA/weather/today/l/62e0efebee1ac0e8fa9b21fd17d57a6a0001753ab6be8a4874bb78bbb52eda02',
'Waterloo' : 'https://weather.com/en-CA/weather/today/l/CAXX0531:1:CA'}

TO_info = lists_to_string('Toronto')
UW_info = lists_to_string('Waterloo')

cities = {'Toronto': TO_info, 'Waterloo' : UW_info}

var = StringVar()

class Display:
    def __init__(self,master):

        '''Creates frame for the weather information'''

        frame = Frame(master, width = 200,padx = 10, pady = 10)
        frame.pack(side = RIGHT)

        '''Creates a label to display temp'''

        self.temp = Label(frame, textvariable = var)
        self.temp.pack()

class Selection:
    def __init__(self,master):

        '''Creates frame for selection of city'''

        frame = Frame(master, width = 100,padx = 10, pady = 10)
        frame.pack(side = LEFT)

        '''Creating all the Radiobutton selections'''

        for place, temp in cities.items():
            self.select = Radiobutton(frame, text = place, variable = var, value = temp,
            indicatoron = 0, width = 25)
            self.select.pack()

Info = Selection(root)
Weather = Display(root)

root.mainloop()
