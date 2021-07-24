from enum import Enum


class LedType(Enum):
    CATHODE = "CATHODE"
    ANODE = "ANODE"


SCOREBOARD_CONFIG = {
    'led_type': LedType.CATHODE,
    'layout': [
        'guest.goals',
        'home.goals',
        'guest.points',
        'home.points',
        'guest.total',
        'home.total',
        'quarter'
    ],
    'timer': {
        'serial_data_input': 11,
        'memory_clock': 12,
        'serial_clock': 13,
        'clock_speed': 0.0001,
        'update_interval': .001

    },
    'scoreboard': {
        'serial_data_input': 11,
        'memory_clock': 12,
        'serial_clock': 13,
        'clock_speed': 0.001
    }
}

DICTIONARY_CONFIG = {
    LedType.ANODE: {
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
    },
    LedType.CATHODE: {
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

    },
}


def get_dictionary():
    return DICTIONARY_CONFIG[SCOREBOARD_CONFIG['led_type']]


def get_layout():
    return SCOREBOARD_CONFIG['layout']


def get_timer_config():
    return SCOREBOARD_CONFIG['timer']


def get_scoreboard_config():
    return SCOREBOARD_CONFIG['scoreboard']
