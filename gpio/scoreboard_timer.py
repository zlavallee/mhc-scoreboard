import logging
from threading import Thread, Event

from config import config
from scoreboard.calculated_timer import MinuteSecondTimer
from gpio.seven_segment_led import SevenSegmentLed, create_seven_segment_led
from util.string_utils import to_padded_string
from util.timer_utils import from_seconds


def create_scoreboard_timer():
    timer_config = config.get_timer_config()
    return ScoreboardTimer(
        led=create_seven_segment_led(timer_config),
        update_interval=timer_config['update_interval'])


def get_minutes_seconds_string(timer):
    (minutes, seconds) = timer.get_minutes_seconds()

    return to_padded_string(minutes, padding_value='_', digits=2), to_padded_string(seconds, digits=2)


def update_timer(wait_time, stop_event: Event, timer: MinuteSecondTimer, output):
    while not stop_event.wait(wait_time):
        (minutes, seconds) = get_minutes_seconds_string(timer)

        logging.info('Updating scoreboard timer to: {}:{}'.format(minutes, seconds))

        output.set_values(minutes + seconds)


class ScoreboardTimer:

    def __init__(self, led: SevenSegmentLed, update_interval):
        self.led_output = led
        self.timer = MinuteSecondTimer()
        self.stop_event = Event()
        self.update_interval = update_interval
        self.timer_thread = self._create_timer_thread()

    def __del__(self):
        if self.timer_thread.is_alive():
            self.stop_event.set()

        self.timer_thread.join(self.update_interval * 10)

    def start_timer_thread(self):
        self.timer_thread.start()

    def start(self):
        logging.info('Starting scoreboard timer.')
        self.timer.start()

    def stop(self):
        logging.info('Stopping scoreboard timer.')
        self.timer.stop()

    def set(self, seconds=0):
        logging.info('Setting scoreboard timer to: {}.'.format(seconds))
        self.timer.set(from_seconds(seconds))

    def get_timer(self):
        return {
            "running": self.timer.running,
            "start_time": self.timer.start_time,
            "offset": self.timer.offset
        }

    def reset(self):
        self.set()

    def clear(self):
        logging.info('Clearing scoreboard timer.')
        self.timer.clear()

    def set_values(self, values):
        self.led_output.set_values(values)

    def _get_minutes_seconds_string(self):
        (minutes, seconds) = self.timer.get_minutes_seconds()

        return to_padded_string(minutes, digits=2), to_padded_string(seconds, digits=2)

    def _create_timer_thread(self):
        return Thread(target=update_timer, args=(self.update_interval, self.stop_event, self.timer, self.led_output),
                      daemon=True)
