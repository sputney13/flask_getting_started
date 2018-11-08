from flask import Flask, jsonify, request
import math
app = Flask(__name__)


@app.route("/name", methods=["GET"])
def get_name():
    name = {
        "name": "Sarah"
    }
    return jsonify(name)


@app.route("/hello/<name>", methods=["GET"])
def hello_name(name):
    message = {
        "message": "Hello there, {}".format(name)
    }
    return jsonify(message)


@app.route("/distance", methods=["POST"])
def distance():
    points = {"a": [1, 2], "b": [2, 3]}
    r = request.get_json(points)
    dist = math.sqrt((r["a"[0]] - r["a"[1]]) ** 2 +
                     (r["b"[0]] - r["b"[1]]) ** 2)
    distance = {
        "distance": dist,
        "a": [r["a"[0]], r["b"[0]]],
        "b": [r["a"[1]], r["b"[1]]]
    }
    return distance


if __name__ == "__main__":
    app.run(host="127.0.0.1")
