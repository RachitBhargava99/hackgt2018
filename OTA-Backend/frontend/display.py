import frontend
from flask import *
import webbrowser

app = Flask(__name__)

output, current_gps = frontend.caller()

maps_url = 'https://maps.googleapis.com/maps/api/staticmap'

maps_key = 'AIzaSyAs5sA8X7MR-vbuNNxfJ4a-xSiUeOLtg-U'
##maps_secret = 'feppmHUuDhJPGvXW8X_fbyPqld4='

markers = []
marker_call = ''

for (index, item) in enumerate(output):
    markers.append('label:' + str(index+1) + '|' + (item['coordinates'])[1:-1])
    marker_call += ('markers=' + 'label:' + str(index+1) + '|' + (item['coordinates'])[1:-1])
    if index != 4:
        marker_call += '&'
    current_coordinates = item['coordinates'].split(',')
    lat, lon = float(current_coordinates[0][1:]), float(current_coordinates[1][:-1])
    item['lyft_lat'], item['lyft_lon'] = lat, lon

gps_coordinates_1 = current_gps.split(',')
gps_lat = float(gps_coordinates_1[0])
gps_lon = float(gps_coordinates_1[1])

map_call = maps_url + '?' + 'center=33.7629,-84.3949' + '&' + 'size=' + '720x480' + '&' + 'zoom=14' + '&' + marker_call + '&' + 'key=' + maps_key
##'&' + 'signature=' + maps_secret
    
    

@app.route('/')
def home():
    return render_template('home.html', posts = output, maps_image = map_call, gps_lat = gps_lat, gps_lon = gps_lon)

webbrowser.open('http://127.0.0.1:80')
app.run(host = '127.0.0.1', port = 80, debug = True, use_reloader = False)
