import logging
import os

import flask
from flask import Flask, send_from_directory, request
from flask_cors import CORS

from scoreboard.scoreboard import create_scoreboard
from setup import setup_logging, initialize, destroy

client_name = "scoreboard-client"

app = Flask(__name__,
            static_folder="./{}/build/".format(client_name))
CORS(app)

initialize()
scoreboard = create_scoreboard()


@app.route('/api/v1.0/reset', methods=['POST'])
def reset_scoreboard():
    logging.info("Resetting scoreboard.")
    scoreboard.reset()

    return flask.jsonify(scoreboard.scoreboard)


@app.route('/api/v1.0/scoreboard', methods=['GET'])
def get_scoreboard():
    scoreboard_state = scoreboard.scoreboard

    logging.info("Getting scoreboard: {}".format(scoreboard_state))

    return flask.jsonify(scoreboard_state)


@app.route('/api/v1.0/scoreboard', methods=['POST'])
def post_scoreboard():
    scoreboard_json = request.get_json()

    logging.info("Updating scoreboard: {}".format(scoreboard_json))

    scoreboard.scoreboard = scoreboard_json

    return flask.jsonify(scoreboard.scoreboard), 200


@app.route('/api/v1.0/timer', methods=['GET'])
def get_timer():
    timer_state = scoreboard.timer

    logging.info("Getting timer: {}".format(timer_state))

    return flask.jsonify(timer_state), 200


@app.route('/api/v1.0/timer', methods=['POST'])
def set_timer():
    timer_json = request.get_json()

    logging.info("Updating timer: {}".format(timer_json))

    scoreboard.timer = timer_json
    return flask.jsonify(scoreboard.timer), 200


@app.route('/api/v1.0/timer/start', methods=['POST'])
def start_timer():
    logging.info("Starting timer.")
    scoreboard.start_timer()

    timer_state = scoreboard.timer

    return flask.jsonify(timer_state), 200


@app.route('/api/v1.0/timer/stop', methods=['POST'])
def stop_timer():
    logging.info("Stopping timer.")
    scoreboard.stop_timer()
    return flask.jsonify(scoreboard.timer), 200


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    logging.info("Serving static path: {}".format(path))

    if path != "" and os.path.exists("{}/build/".format(client_name) + path):
        return send_from_directory('{}/build'.format(client_name), path)
    else:
        return send_from_directory('{}/build'.format(client_name), 'index.html')


def setup():
    setup_logging()


if __name__ == '__main__':
    try:
        setup()
        scoreboard.run_test_sequence()
        scoreboard.initialize()
        app.run(host='0.0.0.0')
    finally:
        destroy()
