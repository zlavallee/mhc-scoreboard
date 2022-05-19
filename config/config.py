from enum import Enum


class LedType(Enum):
    CATHODE = "CATHODE"
    ANODE = "ANODE"


SCOREBOARD_CONFIG = {
    'led_type': LedType.CATHODE,
    'layout': [
        'visitor.goals',
        'home.goals',
        'visitor.points',
        'home.points',
        'visitor.total',
        'home.total',
        'quarter'
    ],
    'timer': {
        'serial_data_input': 15,  # GPIO22
        'memory_clock': 16,  # GPIO23
        'serial_clock': 18,  # GPIO24
        'clock_speed': 0.001,
        'update_interval': .1

    },
    'scoreboard': {
        'serial_data_input': 11,  # GPIO17
        'memory_clock': 12,  # GPIO18
        'serial_clock': 13,  # GPIO27
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
        "0": 0xBF,
        "1": 0x86,
        "2": 0xDB,
        "3": 0xCF,
        "4": 0xE6,
        "5": 0xED,
        "6": 0xFD,
        "7": 0x87,
        "8": 0xFF,
        "9": 0xE7,

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
