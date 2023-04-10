import requests

BASE = "http://127.0.0.1:5000/"

response = requests.post(BASE + "video/1",{"likes":10})
#response = requests.get(BASE + "video/1")

print(response.json())