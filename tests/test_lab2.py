from lab2 import is_odd, is_even, \
    time_elapsed, \
    area, perimeter, volume, surface_area, \
    get_square_color, \
    prettify_time, \
    right_justify, center_justify

import time


def test_odd_ints():
    assert is_odd(42) is False
    assert is_odd(9999) is True


def test_odd_negatives():
    assert is_odd(-10) is False
    assert is_odd(-11) is True


def test_odd_floats():
    assert is_odd(3.1415) is False


def test_even_ints():
    assert is_even(42) is True
    assert is_even(9999) is False


def test_even_negatives():
    assert is_even(-10) is True
    assert is_even(-11) is False


def test_even_floats():
    assert is_even(3.1415) is False


def test_time_elapsed():
    assert time_elapsed(round(time.time())) == (0, 0, 0, 0)
    assert time_elapsed(round(time.time()) - 1) == (0, 0, 0, 1)
    assert time_elapsed(round(time.time()) - 60) == (0, 0, 1, 0)
    assert time_elapsed(round(time.time()) - 60 * 60) == (0, 1, 0, 0)
    assert time_elapsed(round(time.time()) - 24 * 60 * 60) == (1, 0, 0, 0)
    assert time_elapsed(round(time.time()) - (24 * 60 * 60 + 60 * 60 + 60 + 1)) == (1, 1, 1, 1)


def test_area():
    assert area(10, 10) == 100
    assert area(0, 9999) == 0
    assert area(5, 8) == 40


def test_perimeter():
    assert perimeter(10, 10) == 40
    assert perimeter(0, 9999) == 19998
    assert perimeter(5, 8) == 26


def test_volume():
    assert volume(10, 10, 10) == 1000
    assert volume(9999, 0, 9999) == 0
    assert volume(5, 8, 10) == 400


def test_surface_area():
    assert surface_area(10, 10, 10) == 600
    assert surface_area(9999, 0, 9999) == 199960002
    assert surface_area(5, 8, 10) == 340


def test_white_squares():
    assert get_square_color(1, 1) == 'white'
    assert get_square_color(4, 4) == 'white'
    assert get_square_color(7, 7) == 'white'


def test_black_squares():
    assert get_square_color(2, 1) == 'black'
    assert get_square_color(1, 2) == 'black'


def test_non_squares():
    assert get_square_color(0, 8) == ''
    assert get_square_color(2, 9) == ''


def test_prettify_time_strict():
    assert prettify_time(0, 0, 0, 0) == ''
    assert prettify_time(1, 0, 0, 0) == '1 day'
    assert prettify_time(0, 1, 0, 0) == '1 hour'
    assert prettify_time(0, 0, 1, 0) == '1 minute'
    assert prettify_time(0, 0, 0, 1) == '1 second'
    assert prettify_time(1, 2, 0, 5) == '1 day, 2 hours, 5 seconds'


import re


def test_prettify_time_permissive():
    assert re.match(r'^1 days?$', prettify_time(1, 0, 0, 0)) is not None
    assert re.match(r'^1 hours?$', prettify_time(0, 1, 0, 0)) is not None
    assert re.match(r'^1 minutes?$', prettify_time(0, 0, 1, 0)) is not None
    assert re.match(r'^1 seconds?$', prettify_time(0, 0, 0, 1)) is not None
    assert re.match(r'^1 days?, 2 hours, 5 seconds$', prettify_time(1, 2, 0, 5)) is not None


def test_right_justify():
    assert len(right_justify('test', 90)) == 90
    assert len(re.match(r' *', right_justify('test', 90)).group(0)) == 86


def test_right_justify_xl():
    assert len(right_justify('test', 3)) == 4
    assert len(re.match(r' *', right_justify('test', 3)).group(0)) == 0


def test_center_justify():
    fields = re.match(r'( *)[^ ]( *)', center_justify('test', 90))
    left_padding = len(fields.groups(1))
    right_padding = len(fields.groups(3))
    assert abs(left_padding - right_padding) < 2


def test_get_square_color():
    assert get_square_color(1, 1) == 'white'
    assert get_square_color(4, 4) == 'white'
    assert get_square_color(7, 7) == 'white'
