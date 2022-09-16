import random
import sys
from basic_table import db, User
import requests
import os

from datetime import datetime
import pandas as pd
import urllib.parse
import schedule
import time

user_api="e84e9d7d2b7f98a86fbe7c2bd399841d"
#address=input("enter your city name, state,country")

city_list=['Agra Uttar Pradesh','Aligarh Uttar Pradesh','Allahabad  Uttar Pradesh' ,'Ambedkar Nagar Uttar Pradesh','Auraiya Uttar Pradesh','Azamgarh Uttar Pradesh',
'Bahraich Uttar Pradesh','Ballia Uttar Pradesh','Balrampur Uttar Pradesh','Banda Uttar Pradesh','Barabanki Uttar Pradesh','Bareilly Uttar Pradesh',
'Basti Uttar Pradesh','Bijnor Uttar Pradesh','Budaun Uttar Pradesh','Bulandshahr Uttar Pradesh','Chandauli Uttar Pradesh','Chitrakoot Uttar Pradesh','Deoria Uttar Pradesh',
'Etah Uttar Pradesh','Etawah Uttar Pradesh','Faizabad Uttar Pradesh','Farrukhabad Uttar Pradesh','Fatehpur Uttar Pradesh','Firozabad Uttar Pradesh',
'Gautam Buddha Nagar Uttar Pradesh','Ghaziabad Uttar Pradesh','Ghazipur Uttar Pradesh','Gonda Uttar Pradesh','Gorakhpur Uttar Pradesh',
'Hamirpur Uttar Pradesh','Hardoi Uttar Pradesh']


def getdata(city_list):
    final_data = []
    for i in range(len(city_list)):
        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(city_list[i]) + '?format=json'
        response = requests.get(url).json()
        LAT = (response[0]["lat"])
        LON = (response[0]["lon"])
        complete_api_link = "https://api.openweathermap.org/data/2.5/weather?lat=" + LAT + "&lon=" + LON + "&appid=" + user_api
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()

        if api_data['cod'] == '404':
            print("invlid city")
        else:
            db.session.commit()
            user = User(current_temp_city=round(((api_data['main']['temp']) - 273.15), 2),
                    weather_desc=str(api_data['weather'][0]['description']),
                    max_temp_city=round(((api_data['main']['temp_max']) - 273.15), 2),
                    min_temp_city=round(((api_data['main']['temp_min']) - 273.15), 2),
                    pressure=(api_data['main']['pressure']),
                    humidity=(str(api_data['main']['humidity']) + "%"),
                    wind_speed=(str(api_data['wind']['speed']) + "Kmph"),
                    District_state=str(city_list[i].upper()),
                    country=str(api_data['sys']['country']),
                    date_time=str(datetime.now().strftime("%d %b %Y | %I:%M:%S %p")))
        db.session.add(user)
    db.session.commit()


if __name__ == '__main__':
    getdata(city_list)
    #insertMultipleRecords(f)
