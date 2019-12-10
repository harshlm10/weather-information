from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime
# Create your views here.

def home_view(request, *args, **krwgs):
    print(request.user)
    return render(request, 'home.html', {})


def add(request):
    city = request.GET['city']
    city = (city.upper())
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&mode=json&appid=f45b76cca5c93840246d08418f3e7926'.format(city))
    data = r.json()
    forecast = requests.get('https://api.openweathermap.org/data/2.5/forecast?q={}&units=metric&mode=json&appid=f45b76cca5c93840246d08418f3e7926'.format(city))
    forecast_data = forecast.json()
    weather = data['weather'][0]['main']
    weather_icon = data['weather'][0]['icon']
    temprature = data['main']['temp']
    sunrise = data['sys']['sunrise']
    sunrise = datetime.datetime.fromtimestamp(int(sunrise)).strftime('%Y-%m-%d %H:%M:%S')
    sunset = data['sys']['sunset']
    sunset = datetime.datetime.fromtimestamp(int(sunset)).strftime('%Y-%m-%d %H:%M:%S')
    clouds = data['clouds']['all']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    max_temp = data['main']['temp_max']
    min_temp = data['main']['temp_min']
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    wind_degree = data['wind']['deg']
    day1 = forecast_data['list'][0]['dt_txt']
    day2 = forecast_data['list'][6]['dt_txt']
    day3 = forecast_data['list'][14]['dt_txt']
    day4 = forecast_data['list'][22]['dt_txt']
    day5 = forecast_data['list'][30]['dt_txt']
    day1_6 = forecast_data['list'][0]['main']['temp']
    day1_9 = forecast_data['list'][1]['main']['temp']
    day1_12 = forecast_data['list'][2]['main']['temp']
    day1_15 = forecast_data['list'][3]['main']['temp']
    day1_18 = forecast_data['list'][4]['main']['temp']
    day1_21 = forecast_data['list'][5]['main']['temp']
    weather = {
        'weather': weather,
        'weather_icon': weather_icon,
        'temprature': temprature,
        'city': city,
        'sunrise': sunrise[11:],
        'sunset': sunset[11:],
        'clouds': clouds,
        'latitude': latitude,
        'longitude': longitude,
        'max_temp': max_temp,
        'min_temp': min_temp,
        'pressure': pressure,
        'humidity': humidity,
        'wind_speed': wind_speed,
        'wind_degree': wind_degree,
        'day1': day1[0:10],
        'day2': day2[0:10],
        'day3': day3[0:10],
        'day4': day4[0:10],
        'day5': day5[0:10],
        'day1_6': day1_6,
        'day1_9': day1_9,
        'day1_12': day1_12,
        'day1_15': day1_15,
        'day1_18': day1_18,
        'day1_21': day1_21,
        'day2_0': forecast_data['list'][6]['main']['temp'],
        'day2_3': forecast_data['list'][7]['main']['temp'],
        'day2_6': forecast_data['list'][8]['main']['temp'],
        'day2_9': forecast_data['list'][9]['main']['temp'],
        'day2_12': forecast_data['list'][10]['main']['temp'],
        'day2_15': forecast_data['list'][11]['main']['temp'],
        'day2_18': forecast_data['list'][12]['main']['temp'],
        'day2_21': forecast_data['list'][13]['main']['temp'],
    }
    return render(request, 'result.html', weather)