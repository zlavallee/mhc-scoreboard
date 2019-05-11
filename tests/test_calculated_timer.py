from unittest import TestCase

from calculated_timer import NanoSecondTimer

import time


def start_and_wait(timer):
    timer.start()
    time.sleep(.001)


class TestNanoSecondTimer(TestCase):
    def test_timer_initialization(self):
        timer = NanoSecondTimer()
        self.assert_initialization(timer)

    def test_timer_start(self):
        timer = NanoSecondTimer()
        self.assert_initialization(timer)

        start_and_wait(timer)

        self.assertTrue(timer.running)
        self.assertGreater(timer.get_time(), 0)

    def test_timer_start_stop(self):
        timer = NanoSecondTimer()
        self.assert_initialization(timer)

        start_and_wait(timer)
        timer.stop()

        self.assertFalse(timer.running)
        self.assertGreater(timer.get_time(), 0)

        current_time = timer.get_time()

        self.assertEqual(current_time, timer.get_time())
        timer.stop()
        self.assertEqual(current_time, timer.get_time())

    def test_timer_reset(self):
        timer = NanoSecondTimer()
        self.assert_initialization(timer)

        start_and_wait(timer)
        timer.stop()

        self.assertFalse(timer.running)
        self.assertGreater(timer.get_time(), 0)

        current_time = timer.get_time()

        self.assertEqual(current_time, timer.get_time())

        timer.reset()
        self.assertFalse(timer.running)
        self.assertEqual(timer.get_time(), 0)

    def test_timer_set(self):
        timer = NanoSecondTimer()
        self.assert_initialization(timer)

        start_and_wait(timer)
        timer.stop()

        self.assertFalse(timer.running)
        self.assertGreater(timer.get_time(), 0)

        current_time = timer.get_time()

        self.assertEqual(current_time, timer.get_time())

        start_and_wait(timer)
        timer.set(1000)
        self.assertFalse(timer.running)
        self.assertEqual(1000, timer.get_time())

    def assert_initialization(self, timer):
        self.assertFalse(timer.running)
        self.assertEqual(0, timer.get_time())
