# pip install Flask
# pip install requests

from flask import Flask, jsonify, request
import json

HOST = "localhost" # 127.0.0.1
PORT = 1234
DEBUG = True

app = Flask(__name__)
# ROUTE START #
@app.route("/first", methods=["GET"]) # get request
def firstRoute():
    return jsonify({"response":"My first!"})

@app.route("/numberInspector", methods=["POST"])
def numberInspector():
    # looking specifically for an int
    userInput = request.json["value"]
    results = {}
    try:
        results = getDataFor(str(userInput))
    except KeyError:
        results = createDataFor(userInput)
    if (type(userInput) == int):
        return {"results": results}
    else:
        return jsonify({"results": "The \"value\" should be an Integer."}), 400
# ROUTE END # 

def createDataFor(value):
    data = load_data()
    data[value] = {
            "isEven" : value % 2 == 0,
            "square" : value**2,
            "cube" : value ** 3,
            "binary" : bin(value),
            "hex" : hex(value)
        }
    save_data(data)
    return data[value]

def getDataFor(value):
    data = load_data()
    return data[value]

# function to load data
def load_data():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data

# function to save data
def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file)

if __name__ == '__main__':
    app.run(host=HOST, port=PORT, debug=DEBUG)