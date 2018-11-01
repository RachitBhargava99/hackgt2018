import requests
import urllib
import urllib3
import json
import geocoder

def caller():
    URL = "https://hackventure---ha-1539747396872.appspot.com/sorter"
    coordinates = str(geocoder.ip('me').latlng) [1:-1] ##'33.7773, -84.3962'
    preferences, sort = inputs()
    if preferences == -1 or sort == -1:
        pass
    else:
        headers = {
                'Content-Type': 'application/json'
            }

        data = '{"algorithm_num": ' + str(sort) + ', "gps_coordinates": "' + coordinates + '", "user_preference": ' + str(preferences) + '}'

        raw_response = requests.post(url = URL, headers = headers, data = data)
        response = raw_response.json()
        output = response ['rows']
        top_5 = output[:5]
        return (top_5, coordinates)

def inputs():
    print("On a scale of 0 - 10, indicate what does each of the following state apply to you.")
    try:
        user_preference_0 = int(float(input("I'm seeking thrills. ")))
        user_preference_1 = int(float(input("I want to be active. ")))
        user_preference_2 = int(float(input("I want to be engaged. ")))
        user_preference_3 = int(float(input("I want to explore. ")))
        user_preference_4 = int(float(input("I'm seeking party vibes. ")))
        user_preference = [user_preference_0, user_preference_1, user_preference_2, user_preference_3, user_preference_4]
        print()
        print("Awesome! Thanks for letting us know about your mood!")
        print()
        print()
        print("What describes you the best?")
        print("[1] I prefer to travel to places that match closely with my mood.")
        print("[2] I prefer to travel to places that have ideal weather conditions.")
        print("[3] I prefer to travel to places that require the least amount of time to reach.")
        print("[0] I want to visit a random place today! I do not have any preferences.")
        algorithm_num = int(float(input("\nSelect your input: ")))
        if algorithm_num > 3 or algorithm_num < 0 or min(user_preference) < 0 or min(user_preference) > 10:
            raise ValueError("Incorrect Value")
        return(user_preference, algorithm_num)
    except:
        print("Sorry, that's an invalid input!")
        return (-1, -1)

