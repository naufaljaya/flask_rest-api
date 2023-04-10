import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "video/1",{"name": "bruhh", "views":100,"likes":10})
print(response.json())
response = requests.post(BASE + "video/2",{"name": "bruhh", "views":100,"likes":10})
print(response.json())
response = requests.get(BASE + "video/1")
print(response.json())