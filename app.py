from flask import Flask, request, jsonify, json
import collections.abc

app = Flask(__name__)
app.json.sort_keys = False

def recursive_update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = recursive_update(d.get(k, {}), v)
        else:
            d[k] = v
    return d

def recursive_add(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = recursive_add(d.get(k, {}), v)
        else:
            if k in d:
                d[k] += v
            else:
                d[k] = v
    return d

def load_data() -> dict:
    with open("data.json", "r") as file:
        loaded_data : dict = json.load(file)
    return loaded_data

def write_data(new_data):
    with open("data.json", "w") as file:
        json.dump(new_data, file, indent=4)

@app.route('/user_analytics', methods=['GET'])
def get_user_analytics():

    loaded_data = load_data()

    response = loaded_data

    return jsonify(response)

@app.route('/user_analytics/set', methods=['POST'])
def update_user_analytics():

    req_data = request.get_json()

    loaded_data = load_data()

    recursive_update(loaded_data, req_data)

    write_data(loaded_data)

    return jsonify(req_data)

@app.route('/user_analytics/add', methods=['POST'])
def add_user_analytics():

    req_data = request.get_json()

    loaded_data = load_data()

    recursive_add(loaded_data, req_data)

    write_data(loaded_data)

    return jsonify(req_data)

if __name__ == '__main__':
    app.run(port=6001)