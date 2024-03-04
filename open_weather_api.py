#!/usr/bin/env python3

import os
import urllib.request
import json

import urllib.parse #либа для работа url 

def getWeather(city, apiKey):
    city_encoded = urllib.parse.quote(city, encoding='UTF-8') # Далаем кодировку кирилицу в латиницу для запроса 
    print(city, city_encoded)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_encoded}&appId={apiKey}&units=metric&lang=ru"
    with urllib.request.urlopen(url) as result: # Что делать если ошбика 404 
        weacherJson = json.loads(result.read())
        #print(weacherJson)
        return {
            "city": city,
            "feels_like": weacherJson["main"]["feels_like"],
            "wind_speed": weacherJson["wind"]["speed"],
        }

if __name__ == "__main__":
    city = "Minsk"
    apiKey = "Your api key"
    weatherData = getWeather(city, apiKey)
    print(weatherData)


