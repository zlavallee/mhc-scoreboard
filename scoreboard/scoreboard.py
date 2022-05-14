import logging
import time

from gpio.scoreboard_display import create_scoreboard_display
from gpio.scoreboard_timer import create_scoreboard_timer


def create_scoreboard():
    return Scoreboard(
        scoreboard_display=create_scoreboard_display(),
        scoreboard_timer=create_scoreboard_timer()
    )


# TODO: Implement this.
class Scoreboard:
    def __init__(self, scoreboard_display, scoreboard_timer):
        self.scoreboard_display = scoreboard_display
        self.scoreboard_timer = scoreboard_timer

    def initialize(self):
        self.scoreboard_timer.start_timer_thread()
        self.reset()

    def reset(self):
        self.scoreboard_display.update_scoreboard(_initial_scoreboard_state())
        self.scoreboard_timer.reset()

    @property
    def scoreboard(self):
        return self.scoreboard_display.get_scoreboard()

    @scoreboard.setter
    def scoreboard(self, scoreboard):
        self.scoreboard_display.update_scoreboard(scoreboard)

    @property
    def timer(self):
        return self.scoreboard_timer.get_timer()

    @timer.setter
    def timer(self, timer):
        total_seconds = timer.get('minutes', 0) * 60 + timer.get('seconds', 0)
        self.scoreboard_timer.set(total_seconds)

    def start_timer(self):
        self.scoreboard_timer.start()

    def stop_timer(self):
        self.scoreboard_timer.stop()

    def reset_timer(self):
        self.scoreboard_timer.reset()

    def run_test_sequence(self):
        logging.info('Running scoreboard diagnostic.')
        for _ in range(3):
            logging.info("Writing all values...")
            self._write_test_values()
            time.sleep(1)
            logging.info("Clearing scoreboard...")
            self._clear_test_values()
            time.sleep(1)
        logging.info("Diagnostic complete.")

    def _write_test_values(self):
        self.scoreboard_display.update_scoreboard(_create_scoreboard_dict_with("88"))
        self.scoreboard_timer.set_values("8888")

    def _clear_test_values(self):
        self.scoreboard_display.update_scoreboard(_create_scoreboard_dict_with("__"))
        self.scoreboard_timer.set_values("____")


def _create_scoreboard_dict_with(value):
    return {
        "visitor": {
            "points": value,
            "goals": value,
            "total": value
        },
        "home": {
            "points": value,
            "goals": value,
            "total": value
        },
        "quarter": value
    }


def _initial_scoreboard_state():
    return {
        "visitor": {
            "points": "0",
            "goals": "0",
            "total": "0"
        },
        "home": {
            "points": "0",
            "goals": "0",
            "total": "0"
        },
        "quarter": "1"
    }
