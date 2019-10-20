import tempfile
from typing import List
from config import config

from gpio.seven_segment_led import SevenSegmentLed, create_seven_segment_led
import pickle

from util import scoreboard_utils


def create_scoreboard_display():
    layout_config = config.get_layout()
    scoreboard_config = config.get_scoreboard_config()
    return ScoreboardDisplay(
        led=create_seven_segment_led(scoreboard_config),
        layout=layout_config
    )


default_scoreboard_state = {
    'home': {
        'goals': '__',
        'points': '__',
        'total': '__'
    },
    'visitor': {
        'goals': '__',
        'points': '__',
        'total': '__'
    },
    'quarter': '_'
}


class ScoreboardDisplay:

    def __init__(self, led: SevenSegmentLed, layout: List[str]):
        self.led = led
        self.layout = layout
        self.scoreboard_state = None
        self.temp_file = 'scoreboard_state.pickle'

    def update_scoreboard(self, scoreboard):
        self.scoreboard_state = scoreboard_utils.pad_score(scoreboard)
        self.led.set_values(self._create_layout_string())
        self._write_scoreboard_state()

    def get_scoreboard(self):
        if self.scoreboard_state is None:
            self._read_scoreboard_state()

        return scoreboard_utils.strip_scoreboard_state(self.scoreboard_state)

    def _create_layout_string(self):
        ordered_string = ''

        for scoreboard_item in self.layout:
            path = scoreboard_item.split('.')
            result = self.scoreboard_state
            for path_item in path:
                result = result[path_item]

            ordered_string += result

        return ordered_string

    def _read_scoreboard_state(self):
        try:
            with open(self._state_filename()) as handle:
                self.scoreboard_state = pickle.load(handle)
        except FileNotFoundError:
            self.scoreboard_state = default_scoreboard_state
            self._write_scoreboard_state()

    def _write_scoreboard_state(self):
        with open(self._state_filename(), 'wb') as handle:
            pickle.dump(self.scoreboard_state, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def _state_filename(self):
        return '{}/{}'.format(tempfile.gettempdir(), self.temp_file)
