import requests

BASE = "http://127.0.0.1:5000/"

reponse = requests.get(BASE + "helloworld/tono")

print(reponse.json())