import requests, json

url = "http://127.0.0.1:6001/user_analytics"

data = {
    "deaths" : 1,
    "level_data" : {
        "tutorial" : {
            "deaths" : 1
        }
    }
}

# This request adds the respective value to each dictionary attribute
response1 = requests.post(url + "/add", json=data)
print(json.dumps(response1.json(), indent = 4))

data = {
    "deaths" : 1,
    "level_data" : {
        "tutorial" : {
            "deaths" : 1
        }
    }
}

# This request sets the respective value to each dictionary attribute
response2 = requests.post(url + "/set", json=data)
print(json.dumps(response2.json(), indent = 4))

response3 = requests.get(url)
print(json.dumps(response3.json(), indent = 4))