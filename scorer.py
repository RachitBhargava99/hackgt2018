import source
import json
import data_importer
import maps_api_manager
import open_weather_map_api
import requests
import urllib
import urllib3

def get_weather_score(current_data):
    ''' Gets score of one location '''
    data = current_data ['rows']
    for item in data:
        current_weather_id = open_weather_map_api.caller(item ['coordinates'] [1: -1])
        raw_data = data_importer.import_weather_data()
        weather_data = raw_data ['rows']
        score = 100
        for item2 in weather_data:
            if item2 ['id'] == current_weather_id:
                score -= item2 ['score']
                break
        item ['weather_score'] = score

def get_travel_score(gps_coordinates):
    ''' Gets score of all the locations '''
    raw_data = json.loads(maps_api_manager.caller(gps_coordinates))
    data = raw_data ['rows']
    sorted_data = source.sort_data(data)
    for (index, item) in enumerate(sorted_data):
        if index > 20:
            item ['travel_score'] = 0
        else:
            item ['travel_score'] = (20 - index) * 5
    return ({'rows': sorted_data})

def get_preference_score(user_preference, current_data):
    ''' Gets score of all the locations '''
    data = current_data ['rows']
    for item in data:
        item ['preference_score'] = 100 - ((abs(int(item ['thrill']) - int(user_preference[0])) + abs(int(item ['active']) - int(user_preference[1])) + abs(int(item ['engage']) - int(user_preference[2])) + abs(int(item ['explore']) - int(user_preference[3])) + abs(int(item ['vibe']) - int(user_preference[4]))) * 2)
    return current_data

def master_scorer(gps_coordinates, user_preference):
    ''' Gets final scores of all the locations '''
    data = get_travel_score(gps_coordinates)
    get_preference_score(user_preference, data)
    get_weather_score(data)
    return data

def final_scorer(travel, preference, weather, data):
    for item in data ['rows']:
        item ['score'] = (item ['travel_score'] * travel) + (item ['preference_score'] * preference) + (item ['weather_score'] * weather)
    return data
