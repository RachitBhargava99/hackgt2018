import json
import requests
import urllib
import urllib3
import source
import polycoder

maps_key = 'AIzaSyAs5sA8X7MR-vbuNNxfJ4a-xSiUeOLtg-U'

## INPUT TYPE: list, list
## DESCRIPTION: The lists must contain the coordinates of locations.

def caller(current, destination):
    unit = 'imperial'
    url = 'https://maps.googleapis.com/maps/api/distancematrix/'
    out_format = 'json'
    lang = 'en'
    origin_coordinates, destination_coordinates = [], []
    for coordinates in current:
        coordinates_list = coordinates.split(',')
        origin_coordinates.append(str(coordinates_list[0]) + ',' + str(coordinates_list[1]))
    for coordinates in destination:
        coordinates_list = coordinates.split(',')
        destination_coordinates.append(str(coordinates_list[0]) + ',' + str(coordinates_list[1]))
    poly_origin = (polycoder.super_encoder(origin_coordinates))
    poly_destination = (polycoder.super_encoder(destination_coordinates))
    add = 'units=' + unit + '&' + 'origins=' + 'enc:' + poly_origin + ':' + '&' + 'destinations=' + 'enc:' + poly_destination + ':' + '&' + 'language=' + lang + '&' + 'key=' + str(maps_key)
##    string_request = url + out_format + '?' + source.http_string_convertor(add)
    request = url + out_format + '?' + add
    response = requests.get(request)
    response_dict = response.json()
    return response_dict

def time_calc(response):
    num_sec = response ['rows'] [0] ['elements'] [0] ['duration'] ['value']
    minutes, seconds = second_splitter(num_sec)
    return (minutes, seconds)

def second_splitter(num_sec):
    minutes = num_sec // 60
    seconds = num_sec % 60
    return (minutes, seconds)

def independent_response():
    current = input("Enter the coordinates of the origin: ")
    destination = input("Enter the coordinates of the destination: ")
    response = distance_calc(current, destination)
    minutes, seconds = time_calc(response)
    print ("It would take", minutes, "minutes and", seconds, "seconds to drive from the origin to the destination.")

##def caller(current, destination):
##    response = distance_calc(current, destination)
##    minutes, seconds = time_calc(response)
##    return (minutes, seconds)
