# First Test Program in Firebase
# Mr. Jugoon
# Program adapted from Stack Overflow example

import requests
from firebase import firebase

# Using Firebase

firebase = firebase.FirebaseApplication('https://ucc2019-c4356.firebaseio.com', None)
result1 = firebase.get('/teacher', None)
print (result1)
result2 = firebase.get('/classes/y9coding/students', None)
print (result2)

# Using JSON Requests

response = requests.get("https://ucc2019-c4356.firebaseio.com/address.json")

if (response.status_code == 200):
        
        # load as a JSON to access specific data more easily
        datajson = response.json()
        print (response)
        print (datajson)
