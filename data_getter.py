import source
import data_importer
import maps_distance_api

def get_coordinates():
    raw_data = data_importer.import_data() ['rows']
    coordinates_data, coordinates = [], []
    for item in raw_data:
        coordinates_data.append((item['id'], item['coordinates']))
        coordinates.append(item['coordinates'])
    return coordinates

def get_data_maps_api(current_gps):
    coordinates = get_coordinates()
    data = maps_distance_api.caller([current_gps], coordinates)
    return data
