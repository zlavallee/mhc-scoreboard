from datetime import time
from enum import Enum

from hurling import Game


class Scoreboard:
    def __init__(self, home_team, visiting_team):
        self.game = Game(home_team, visiting_team)
        self.__driver = ScoreboardDriver()

    @property
    def current_time(self):
        return 0

    @current_time.setter
    def current_time(self, current_time):
        print("Not Implemented")

    def start_timer(self):
        raise NotImplementedError

    def stop_timer(self):
        raise NotImplementedError

    def reset_timer(self):
        raise NotImplementedError


class ScoreboardDriver:
    def __init__(self, start=0):
        self.time = start


class Timer:
    def __init__(self, start=time()):
        self.state = TimerState.INITIALIZE
        self.__current_time = start
        self.__start_time = None
        self.__stop_time = None

    @property
    def current_time(self):
        if self.state == TimerState.RUNNING:
            raise NotImplementedError

        return self.__current_time

    @current_time.setter
    def current_time(self, current_time):
        if self.state == TimerState.STOPPED:
            self.__current_time = current_time
        else:
            raise NotImplementedError

    @property
    def time_reference(self):
        return TimeInstance(self.current_time)

    def start(self):
        self.state = TimerState.RUNNING
        self.__start_time = time()

    def stop(self):
        self.state = TimerState.STOPPED
        self.__current_time = (time() - self.__start_time) + self.__current_time


class TimeInstance:
    def __init__(self, current_time, time_reference=time()):
        self.current_time = current_time
        self.time_reference = time_reference


class TimerState(Enum):
    INITIALIZE = "INITIALIZED"
    RUNNING = "RUNNING"
    STOPPED = "STOPPED"
