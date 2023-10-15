import requests

#the app.route that we use in POST method
url = "http://localhost:9696/predict"


client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
response = requests.post(url, json=client).json()

print(response)