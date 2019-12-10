from django.shortcuts import render
import requests #For Requesting The Api End Point
import datetime #To Convert The Unix Time To Current TIme
# Create your views here.

def home_view(request, *args, **krwgs):
    return render(request, 'home.html', {})
#renders The home.html Page

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

    x = forecast_data['list'][0]['dt_txt']
    x = x[11:13]
    x = int(x)
    x = x//3
    y = 8-x
    day1 = forecast_data['list'][y]['dt_txt']
    day2 = forecast_data['list'][y+8]['dt_txt']
    day3 = forecast_data['list'][y+16]['dt_txt']
    day4 = forecast_data['list'][y+24]['dt_txt']
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
        'day1_0': forecast_data['list'][y]['main']['temp'],
        'day1_3': forecast_data['list'][y+1]['main']['temp'],
        'day1_6': forecast_data['list'][y+2]['main']['temp'],
        'day1_9': forecast_data['list'][y+3]['main']['temp'],
        'day1_12': forecast_data['list'][y+4]['main']['temp'],
        'day1_15': forecast_data['list'][y+5]['main']['temp'],
        'day1_18': forecast_data['list'][y+6]['main']['temp'],
        'day1_21': forecast_data['list'][y+7]['main']['temp'],
        'day2_0': forecast_data['list'][y+8]['main']['temp'],
        'day2_3': forecast_data['list'][y+9]['main']['temp'],
        'day2_6': forecast_data['list'][y+10]['main']['temp'],
        'day2_9': forecast_data['list'][y+11]['main']['temp'],
        'day2_12': forecast_data['list'][y+12]['main']['temp'],
        'day2_15': forecast_data['list'][y+13]['main']['temp'],
        'day2_18': forecast_data['list'][y+14]['main']['temp'],
        'day2_21': forecast_data['list'][y+15]['main']['temp'],
        'day3_0': forecast_data['list'][y+16]['main']['temp'],
        'day3_3': forecast_data['list'][y+17]['main']['temp'],
        'day3_6': forecast_data['list'][y+18]['main']['temp'],
        'day3_9': forecast_data['list'][y+19]['main']['temp'],
        'day3_12': forecast_data['list'][y+20]['main']['temp'],
        'day3_15': forecast_data['list'][y+21]['main']['temp'],
        'day3_18': forecast_data['list'][y+22]['main']['temp'],
        'day3_21': forecast_data['list'][y+23]['main']['temp'],
        'day4_0': forecast_data['list'][y+24]['main']['temp'],
        'day4_3': forecast_data['list'][y+25]['main']['temp'],
        'day4_6': forecast_data['list'][y+26]['main']['temp'],
        'day4_9': forecast_data['list'][y+27]['main']['temp'],
        'day4_12': forecast_data['list'][y+28]['main']['temp'],
        'day4_15': forecast_data['list'][y+29]['main']['temp'],
        'day4_18': forecast_data['list'][y+30]['main']['temp'],
        'day4_21': forecast_data['list'][y+31]['main']['temp'],
    }
    return render(request, 'result.html', weather)
