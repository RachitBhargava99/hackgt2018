import source
import data_importer
import maps_distance_api
import data_getter
import json

def caller(gps_coordinates):
    maps_data = data_getter.get_data_maps_api(gps_coordinates)
    raw_data = data_importer.import_data() ['rows']
    final = {}
    final ['rows'] = []
    for (index, element) in enumerate(maps_data ['rows'] [0] ['elements']):
        data = raw_data [index]
        final ['rows'].append({
            'id': index,
            'name': data ['name'],
            'address': data ['address'],
            'coordinates': ('(' + data ['coordinates'] + ')'),
            'distance': element ['distance'] ['value'],
            'duration': element ['duration'] ['value'],
            'thrill': data ['thrill'],
            'active': data ['active'],
            'engage': data ['engage'],
            'explore': data ['explore'],
            'vibe': data ['vibe']
            }
                              )
    output = json.dumps(final)
    return output
