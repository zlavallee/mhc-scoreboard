import math


def to_seconds(nano_seconds):
    return nano_seconds / 1000000000


def from_seconds(seconds):
    return seconds * 1000000000


def get_minutes(seconds):
    return math.floor(seconds / 60)


def get_seconds(seconds):
    return seconds % 60
