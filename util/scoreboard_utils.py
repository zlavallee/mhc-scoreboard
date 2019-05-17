from util import string_utils


def pad_scoreboard_state(scoreboard):
    return {
        'home': pad_score(scoreboard['home']),
        'visitor': pad_score(scoreboard['visitor']),
        'quarter': string_utils.to_padded_string(scoreboard['quarter'], '_', 1)
    }


def strip_scoreboard_state(scoreboard):
    return {
        'home': strip_score(scoreboard['home']),
        'visitor': strip_score(scoreboard['visitor']),
        'quarter': scoreboard['quarter'].replace('_', '')
    }


def strip_score(score):
    new_score = {}

    for key, value in score.items():
        new_score[key] = value.replace('_', '')

    return new_score


def pad_score(score):
    new_score = {}

    for key, value in score.items():
        new_score[key] = string_utils.to_padded_string(value, '_', 2)

    return new_score
