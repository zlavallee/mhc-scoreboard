from util.timer_utils import to_seconds, get_seconds, get_minutes, get_time_ns


class NanoSecondTimer:
    def __init__(self):
        self.running = False
        self.start_time = None
        self.offset = 0

    def start(self):
        if self.running:
            return

        self.running = True
        self.start_time = get_time_ns()

    def get_time(self):
        if not self.running:
            return self.offset

        return self._get_calculated_time()

    def stop(self):
        if not self.running:
            return

        self.offset = self._get_calculated_time()
        self.running = False

    def set(self, nano_seconds=0):
        self.running = False
        self.offset = nano_seconds

    def reset(self):
        self.set()

    def _get_calculated_time(self):
        return (get_time_ns() - self.start_time) + self.offset


class MinuteSecondTimer(NanoSecondTimer):
    def __init__(self):
        super().__init__()

    def get_minutes_seconds(self):
        seconds = to_seconds(self.get_time())

        return get_minutes(seconds), get_seconds(seconds)

    def get_seconds(self):
        return get_seconds(to_seconds(self.get_time()))

    def get_minutes(self):
        return get_minutes(to_seconds(self.get_time()))
