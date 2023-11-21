# strings.py

def print_string(string):
    print(string)


def concatenate(string1, string2):
    return string1 + string2


def format_string(string, *values):
    return string.format(*values)


def string_length(string):
    return len(string)


def slice_substring(string, start, end):
    return string[start:end]


def contains_substring(string, substring):
    return substring in string


def replace_substring(string, old, new):
    return string.replace(old, new)


def convert_to_uppercase(string):
    return string.upper()


def string_is_numeric(string):
    return string.isnumeric()
