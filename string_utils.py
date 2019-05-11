def to_string(number: int, padding_value='0', digits=None):
    if digits is None:
        digits = len(str(number))

    string_number = str(number).rjust(digits, padding_value)

    if len(string_number) == digits:
        return string_number

    return string_number[len(string_number) - digits:len(string_number)]
