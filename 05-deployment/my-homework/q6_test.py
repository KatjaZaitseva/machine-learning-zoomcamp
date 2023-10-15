import requests

#the app.route that we use in POST method
url = "http://localhost:9696/predict"


client = {"job": "retired", "duration": 445, "poutcome": "success"}
response = requests.post(url, json=client).json()

print(response)