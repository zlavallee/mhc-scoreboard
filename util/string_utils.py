def to_padded_string(number, padding_value='0', digits=None):
    if number is None:
        number = padding_value

    if digits is None:
        if number is None:
            digits = 1
        else:
            digits = len(str(number))

    string_number = str(number).rjust(digits, padding_value)

    if len(string_number) == digits:
        return string_number

    return string_number[len(string_number) - digits:len(string_number)]
