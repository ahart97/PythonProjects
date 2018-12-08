from bs4 import BeautifulSoup
import requests
import PySimpleGUI as sg

def get_future_forcast(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    future_forcast = soup.find(class_='looking-ahead')
    return future_forcast

def get_day_forcast(future_forcast):
    
