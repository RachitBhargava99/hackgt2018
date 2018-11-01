import source
import json

def import_data():
    raw_data = open('data.json')
    final_data = json.load(raw_data)
    return(final_data)

def import_weather_data():
    raw_data = open('weather_score_data.json')
    final_data = json.load(raw_data)
    return(final_data)
