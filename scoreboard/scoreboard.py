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

    @property
    def scoreboard(self):
        return self.scoreboard_display.get_scoreboard()

    @scoreboard.setter
    def scoreboard(self, scoreboard):
        self.scoreboard.update_scoreboard(scoreboard)

    @property
    def timer(self):
        return self.scoreboard_timer.get_timer()

    @timer.setter
    def timer(self, timer):
        self.scoreboard_timer.set(timer)

    def start_timer(self):
        self.scoreboard_timer.start()

    def stop_timer(self):
        self.scoreboard_timer.stop()

    def reset_timer(self):
        self.scoreboard_timer.reset()

    def run_test_sequence(self):
        logging.info('Running scoreboard diagnostic.')
        for _ in range(3):
            self._write_test_values()
            time.sleep(1)
            self._clear_test_values()
            time.sleep(1)

    def _write_test_values(self):
        self.scoreboard.update_scoreboard(_create_scoreboard_dict_with("88"))
        self.scoreboard_timer.set_values("8888")

    def _clear_test_values(self):
        self.scoreboard.update_scoreboard(_create_scoreboard_dict_with("__"))
        self.scoreboard_timer.set_values("____")


def _create_scoreboard_dict_with(value):
    return {
        "guest": {
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
