import scorer
import flask
import requests
import json

app = flask.Flask(__name__)

@app.route('/sorter', methods = ['GET', 'POST'])
def sorter():
    ''' Tester: algorithm_num = 0, gps_coordinates = '33.7773, -84.3962', user_preference = [8, 5, 6, 9, 5]'''
    request_json = flask.request.get_json()
##    return json.dumps(request_json)
    algorithm_num = request_json['algorithm_num']
    gps_coordinates = request_json['gps_coordinates']
    user_preference = request_json['user_preference']
    data = scorer.master_scorer(gps_coordinates, user_preference)
    if algorithm_num == 0:
        output = sort_0(data)
    elif algorithm_num == 1:
        output = sort_1(data)
    elif algorithm_num == 2:
        output = sort_2(data)
    elif algorithm_num == 3:
        output = sort_3(data)
    return json.dumps(output)

def sort_0(raw_data):
    return(overall_sort(scorer.final_scorer((1/3), (1/3), (1/3), raw_data)))

def sort_1(raw_data):
    return(overall_sort(scorer.final_scorer((1/4), (1/2), (1/4), raw_data)))

def sort_2(raw_data):
    return(overall_sort(scorer.final_scorer((1/4), (1/4), (1/2), raw_data)))

def sort_3(raw_data):
    return(overall_sort(scorer.final_scorer((1/2), (1/4), (1/4), raw_data)))

def overall_sort(raw_data):
    dummy, final = [], []
    for item in raw_data ['rows']:
        dummy.append((item ['score'], item ['id']))
    dummy.sort(reverse = True)
    for (score, index) in dummy:
        for item2 in raw_data ['rows']:
            if index == item2 ['id']:
                final.append(item2)
                break
    output = {'rows': final}
    return output

#data = json.load(open('data.json'))

@app.route('/tester', methods = ['GET'])
def tester():
    return 'Hello World'

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 8080, debug = True)
