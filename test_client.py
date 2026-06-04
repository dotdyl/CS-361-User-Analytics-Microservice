import requests, json

url = "http://127.0.0.1:6001/user_analytics"

data = {
    "add" : {"deaths" : 1}
}

response1 = requests.post(url, json=data)
print(json.dumps(response1.json(), indent = 4))

data = {
    "add" : {"kills" : 3}
}

response2 = requests.post(url, json=data)
print(json.dumps(response2.json(), indent = 4))

response3 = requests.get(url)
print(json.dumps(response3.json(), indent = 4))