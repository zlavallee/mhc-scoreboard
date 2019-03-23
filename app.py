import os

import flask
from flask import Flask, send_from_directory, request, json, Response

client_name = "scoreboard-client"

app = Flask(__name__,
            static_folder="./{}/build/".format(client_name))

scoreboard = {
    'home': {
        'goals': 2,
        'points': 1,
        'total': 10
    },
    'visitor': {
        'goals': 5,
        'points': 0,
        'total': 10
    },
    'quarter': 1
}


@app.route('/api/v1.0/scoreboard', methods=['GET'])
def get_scoreboard():
    print("GET Scoreboard: ", scoreboard)
    return flask.jsonify(scoreboard)


@app.route('/api/v1.0/scoreboard', methods=['POST'])
def post_scoreboard():
    scoreboard_json = request.get_json()
    print("POST Scoreboard: ", scoreboard_json)

    return flask.jsonify(scoreboard_json), 200


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("{}/build/".format(client_name) + path):
        return send_from_directory('{}/build'.format(client_name), path)
    else:
        return send_from_directory('{}/build'.format(client_name), 'index.html')


if __name__ == '__main__':
    app.run()
