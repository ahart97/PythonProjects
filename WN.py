from bs4 import BeautifulSoup
import requests
import PySimpleGUI as sg

def get_future_forcast(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    future_forcast = soup.find(class_='looking-ahead')
    return seven_day

seven_day = get_future_forcast("https://weather.com/en-CA/weather/today/l/CAON4756:1:CA")
print(seven_day)
