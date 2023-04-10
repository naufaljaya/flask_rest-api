import requests
import random

BASE = "http://127.0.0.1:5000/"
data = [{"name": "name1", "views":random.randint(1,1000000),"likes":random.randint(1,1000000)},
        {"name": "name2", "views":random.randint(1,1000000),"likes":random.randint(1,1000000)},
        {"name": "Joe mama", "views":random.randint(1,1000000),"likes":random.randint(1,1000000)}]

for i in range(len(data)):
    response = requests.post(BASE + "video/" + str(i),data[i])
    print("post requests : ",response.json())

response = requests.delete(BASE + "video/0")
print("delete requests : ",response)

response = requests.get(BASE + "video/2")
print("get requests : ", response.json())