"""Lab 2

Module implementing functions for Odd & Even, Time, Space, Board Square Color,
       Pretty Print, and Justification

  Completed by Matthew Butler on 2024-08-30 for DS-1043"""
import time

Number = int | float  # Number variables can be either int or float
SECONDS_PER_DAY = 60 * 60 * 24
SECONDS_PER_HOUR = 60 * 60
SECONDS_PER_MINUTE = 60


def is_odd(number: Number) -> bool:
    """Returns true if number is an odd integer."""
    return number % 2 == 1


def is_even(number: Number) -> bool:
    """Returns true if number is an even integer."""
    return number % 2 == 0


def time_elapsed(timestamp: int) -> tuple[int, int, int, int]:
    """Returns the (days, hours, minutes, seconds) between now and timestamp,
       which is in seconds since Epoch"""
    elapsed: int = abs(round(time.time()) - timestamp)
    days: int = elapsed // SECONDS_PER_DAY
    elapsed = elapsed % SECONDS_PER_DAY
    hours: int = elapsed // SECONDS_PER_HOUR
    elapsed = elapsed % SECONDS_PER_HOUR
    minutes: int = elapsed // SECONDS_PER_MINUTE
    seconds: int = elapsed % SECONDS_PER_MINUTE
    return days, hours, minutes, seconds  # Note that this creates a tuple and returns it


def area(length: Number, width: Number) -> Number:
    """Returns the area of a rectangle described by length and width."""
    return length * width


def perimeter(length: Number, width: Number) -> Number:
    """Returns the perimeter of a rectangle described by length and width"""
    return (length + width) * 2


def volume(length: Number, width: Number, height: Number) -> Number:
    """Returns the volume of a right rectangular prism described by length, width, and height"""
    return area(length, width) * height


def surface_area(length: Number, width: Number, height: Number) -> Number:
    """Returns the surface area of a right rectangular prism described by length, width, and height"""
    return 2 * (area(length, width) + area(width, height) + area(height, length))


def get_square_color(column: int, row: int) -> str:
    """Returns the color of square described by the coordinates column, row"""
    if 0 <= column <= 7 and 0 <= row <= 7:
        if is_even(column) and is_even(row):
            return 'white'
        elif is_odd(column) and is_odd(row):
            return 'white'
        else:
            return 'black'
    return ''


def pluralize(quantity: int, noun: str) -> str:
    if quantity != 1:
        return noun + 's'
    return noun


def prettify_time(days: int, hours: int, minutes: int, seconds: int) -> str:
    """Returns a string describing the time described by days, hours, minutes, seconds."""
    pretty = ''
    if days > 0:
        pretty = pretty + str(days) + ' ' + pluralize(days, 'day')
        if hours > 0 or minutes > 0 or seconds > 0:
            pretty = pretty + ', '
        else:
            return pretty
    if hours > 0:
        pretty = pretty + str(hours) + ' ' + pluralize(hours, 'hour')
        if minutes > 0 or seconds > 0:
            pretty = pretty + ', '
        else:
            return pretty
    if minutes > 0:
        pretty = pretty + str(minutes) + ' ' + pluralize(minutes, 'minute')
        if seconds > 0:
            pretty = pretty + ', '
        else:
            return pretty
    if seconds > 0:
        pretty = pretty + str(seconds) + ' ' + pluralize(seconds, 'second')
    return pretty


def right_justify(content: str, width: int) -> str:
    """Returns a right justified string containing content relative to column size width"""
    if len(content) > width:
        return content
    padding = ' ' * (width - len(content))
    return padding + content


def center_justify(content: str, width: int) -> str:
    """Returns a center justified string containing content relative to column size width"""
    if len(content) > width:
        return content
    padding = ' ' * ((width - len(content)) // 2)
    return padding + content
