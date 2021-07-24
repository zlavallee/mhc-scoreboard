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

