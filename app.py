from flask import Flask, request, jsonify, json

app = Flask(__name__)
app.json.sort_keys = False

def increment_values(loaded_data, increments):

    for data in increments:
        curr_value = loaded_data.get(data)
        if curr_value is not None:
            loaded_data[data] = curr_value + 1
        else:
            loaded_data[data] = 1

@app.route('/user_analytics', methods=['GET'])
def get_user_analytics():

    with open("data.json", "r") as file:
        loaded_data = json.load(file)

    print(loaded_data)
    response = loaded_data

    return jsonify(response)

@app.route('/user_analytics', methods=['POST'])
def post_user_analytics():

    req_data = request.get_json()

    with open("data.json", "r") as file:
        loaded_data : dict = json.load(file)

    increments =  req_data.get("add", {})

    increment_values(loaded_data, increments)

    with open("data.json", "w") as file:
        json.dump(loaded_data, file, indent=4)

    return jsonify(req_data)

if __name__ == '__main__':
    app.run(port=6001)