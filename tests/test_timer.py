from datetime import time
from unittest import TestCase

from scoreboard import Timer, TimerState


class TestTimer(TestCase):
    def time_test(self):
        self.assertEqual(time(), time())

    def test_timer_initialization_default(self):
        timer = Timer()
        self.assertEqual(TimerState.INITIALIZE, timer.state)
        self.assertEqual(time(), timer.current_time)

    def test_timer_initialization(self):
        timer = Timer(start)
        self.assertEqual(TimerState.INITIALIZE, timer.state)
        self.assertEqual(time.time(), timer.current_time)

