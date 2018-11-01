import source
import json
import requests
import urllib
import urllib3

weather_key = 'a3cec8a61c16b3e33e90aa3079110077'

def caller(gps_coordinates):
    coordinates = gps_coordinates.split(',')
    lat = float(coordinates[0])
    lon = float(coordinates[1])
    url = 'https://api.openweathermap.org/data/2.5/weather'
    request = url + '?' + 'lat=' + str(lat) + '&' + 'lon=' + str(lon) + '&' + 'appid=' + weather_key
    response = requests.get(request)
    response_dict = response.json()
    weather_info, weather_id = response_dict ['weather'] [0] ['main'], response_dict ['weather'] [0] ['id']
    return weather_id
