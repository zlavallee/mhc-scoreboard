from threading import Thread, Event

from calculated_timer import MinuteSecondTimer
from gpio_adapter import SN74HC595NOutput
from seven_segment_led import SevenSegmentLed
from string_utils import to_string
from timer_utils import from_seconds

cathode_digit_dictionary = {
    "_": 0x00,
    "0": 0x3F,
    "1": 0x06,
    "2": 0x5B,
    "3": 0x4F,
    "4": 0x66,
    "5": 0x6D,
    "6": 0x7D,
    "7": 0x07,
    "8": 0x7F,
    "9": 0x67,
}

anode_digit_dictionary = {
    "_": 0xFF,
    "0": 0xC0,
    "1": 0xF9,
    "2": 0xA4,
    "3": 0xB0,
    "4": 0x99,
    "5": 0x92,
    "6": 0x82,
    "7": 0xF8,
    "8": 0x80,
    "9": 0x98,
}


def get_minutes_seconds_string(timer):
    (minutes, seconds) = timer.get_minutes_seconds()

    return to_string(minutes, padding_value='_', digits=2), to_string(minutes, digits=2)


def update_timer(timer: MinuteSecondTimer, output: SevenSegmentLed):
    (minutes, seconds) = get_minutes_seconds_string(timer)
    print('Updating timer to: {}:{}'.format(minutes, seconds))
    output.set_values(minutes.join(seconds))


class ScoreboardTimer:

    def __init__(self, output_device: SN74HC595NOutput, digit_dictionary=None, update_interval=.001):
        if digit_dictionary is None:
            digit_dictionary = anode_digit_dictionary

        self.led_output = SevenSegmentLed(output_device, digit_dictionary)
        self.timer = MinuteSecondTimer()
        self.stop_event = Event()
        self.update_interval = update_interval
        self.timer_thread = self._create_timer_thread()
        self.timer_thread.start()

    def __del__(self):
        if self.timer_thread.is_alive():
            self.stop_event.set()

        self.timer_thread.join(self.update_interval * 10)

    def start(self):
        print('Starting...')
        self.timer.start()

    def stop(self):
        print('Stopping...')
        self.timer.stop()

    def set(self, seconds=0):
        print('Setting time: {}'.format(seconds))
        self.timer.set(from_seconds(seconds))

    def reset(self):
        self.set()

    def _update_timer(self):
        (minutes, seconds) = self._get_minutes_seconds_string()
        print('Updating timer to: {}:{}'.format(minutes, seconds))
        self.led_output.set_values(minutes.join(seconds))

    def _get_minutes_seconds_string(self):
        (minutes, seconds) = self.timer.get_minutes_seconds()

        return to_string(minutes, padding_value='_', digits=2), to_string(minutes, digits=2)

    def _create_timer_thread(self):
        return ScoreboardTimerThread(update_timer, (self.timer, self.led_output), self.stop_event, self.update_interval)


class ScoreboardTimerThread(Thread):
    def __init__(self, target, args, event: Event, wait_time):
        Thread.__init__(self, target=target, args=args)
        self.stopped = event
        self.wait_time = wait_time

    def run(self):
        while not self.stopped.wait(self.wait_time):
            super(ScoreboardTimerThread, self).run()
