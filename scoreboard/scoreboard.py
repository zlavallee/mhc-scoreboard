from gpio.scoreboard_display import create_scoreboard_display
from gpio.scoreboard_timer import create_scoreboard_timer


def create_scoreboard():
    return Scoreboard(
        scoreboard_display=create_scoreboard_display(),
        scoreboard_timer=create_scoreboard_timer()
    )


class Scoreboard:
    def __init__(self, scoreboard_display, scoreboard_timer):
        self.scoreboard_display = scoreboard_display
        self.scoreboard_timer = scoreboard_timer

    @property
    def scoreboard(self):
        return 0

    @scoreboard.setter
    def scoreboard(self, scoreboard):
        print("Not Implemented")

    @property
    def timer(self):
        return 0

    @timer.setter
    def timer(self, timer):
        print("Not Implemented")

    def start_timer(self):
        raise NotImplementedError

    def stop_timer(self):
        raise NotImplementedError

