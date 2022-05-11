import os

import flask
from flask import Flask, send_from_directory, request

from scoreboard.scoreboard import create_scoreboard
from setup import setup_logging, initialize, destroy

client_name = "scoreboard-client"

app = Flask(__name__,
            static_folder="./{}/build/".format(client_name))

initialize()
scoreboard = create_scoreboard()


@app.route('/api/v1.0/scoreboard', methods=['GET'])
def get_scoreboard():
    return flask.jsonify(scoreboard.scoreboard)


@app.route('/api/v1.0/scoreboard', methods=['POST'])
def post_scoreboard():
    scoreboard_json = request.get_json()
    scoreboard.scoreboard = scoreboard_json

    return flask.jsonify(scoreboard.scoreboard), 200


@app.route('/api/v1.0/timer', methods=['GET'])
def get_timer():
    return flask.jsonify(scoreboard.timer), 200


@app.route('/api/v1.0/timer', methods=['POST'])
def set_timer():
    timer_json = request.get_json()
    scoreboard.timer = timer_json
    return flask.jsonify(scoreboard.timer), 200


@app.route('/api/v1.0/timer/start', methods=['POST'])
def start_timer():
    scoreboard.start_timer()
    return 200


@app.route('/api/v1.0/timer/stop', methods=['POST'])
def stop_timer():
    scoreboard.stop_timer()
    return 200


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("{}/build/".format(client_name) + path):
        return send_from_directory('{}/build'.format(client_name), path)
    else:
        return send_from_directory('{}/build'.format(client_name), 'index.html')


def setup():
    print('Setting mode')
    setup_logging()


if __name__ == '__main__':
    try:
        setup()
        scoreboard.run_test_sequence()
        app.run(host='0.0.0.0')
    finally:
        destroy()
