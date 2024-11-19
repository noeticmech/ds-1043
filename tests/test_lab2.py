from .. import lab2

import time


def test_odd_ints():
    assert lab2.is_odd(42) is False
    assert lab2.is_odd(9999) is True


def test_odd_negatives():
    assert lab2.is_odd(-10) is False
    assert lab2.is_odd(-11) is True


def test_odd_floats():
    assert lab2.is_odd(3.1415) is False


def test_even_ints():
    assert lab2.is_even(42) is True
    assert lab2.is_even(9999) is False


def test_even_negatives():
    assert lab2.is_even(-10) is True
    assert lab2.is_even(-11) is False


def test_even_floats():
    assert lab2.is_even(3.1415) is False


def test_time_elapsed():
    assert lab2.time_elapsed(round(time.time())) == (0, 0, 0, 0)
    assert lab2.time_elapsed(round(time.time()) - 1) == (0, 0, 0, 1)
    assert lab2.time_elapsed(round(time.time()) - 60) == (0, 0, 1, 0)
    assert lab2.time_elapsed(round(time.time()) - 60 * 60) == (0, 1, 0, 0)
    assert lab2.time_elapsed(round(time.time()) - 24 * 60 * 60) == (1, 0, 0, 0)
    assert lab2.time_elapsed(round(time.time()) - (24 * 60 * 60 + 60 * 60 + 60 + 1)) == (1, 1, 1, 1)


def test_area():
    assert lab2.area(10, 10) == 100
    assert lab2.area(0, 9999) == 0
    assert lab2.area(5, 8) == 40


def test_perimeter():
    assert lab2.perimeter(10, 10) == 40
    assert lab2.perimeter(0, 9999) == 19998
    assert lab2.perimeter(5, 8) == 26


def test_volume():
    assert lab2.volume(10, 10, 10) == 1000
    assert lab2.volume(9999, 0, 9999) == 0
    assert lab2.volume(5, 8, 10) == 400


def test_surface_area():
    assert lab2.surface_area(10, 10, 10) == 600
    assert lab2.surface_area(9999, 0, 9999) == 199960002
    assert lab2.surface_area(5, 8, 10) == 340


def test_white_squares():
    assert lab2.get_square_color(1, 1) == 'white'
    assert lab2.get_square_color(4, 4) == 'white'
    assert lab2.get_square_color(7, 7) == 'white'


def test_black_squares():
    assert lab2.get_square_color(2, 1) == 'black'
    assert lab2.get_square_color(1, 2) == 'black'


def test_non_squares():
    assert lab2.get_square_color(0, 8) == ''
    assert lab2.get_square_color(2, 9) == ''


def test_prettify_time_strict():
    assert lab2.prettify_time(0, 0, 0, 0) == ''
    assert lab2.prettify_time(1, 0, 0, 0) == '1 day'
    assert lab2.prettify_time(0, 1, 0, 0) == '1 hour'
    assert lab2.prettify_time(0, 0, 1, 0) == '1 minute'
    assert lab2.prettify_time(0, 0, 0, 1) == '1 second'
    assert lab2.prettify_time(1, 2, 0, 5) == '1 day, 2 hours, 5 seconds'


import re


def test_prettify_time_permissive():
    assert re.match(r'^1 days?$', lab2.prettify_time(1, 0, 0, 0)) is not None
    assert re.match(r'^1 hours?$', lab2.prettify_time(0, 1, 0, 0)) is not None
    assert re.match(r'^1 minutes?$', lab2.prettify_time(0, 0, 1, 0)) is not None
    assert re.match(r'^1 seconds?$', lab2.prettify_time(0, 0, 0, 1)) is not None
    assert re.match(r'^1 days?, 2 hours, 5 seconds$', lab2.prettify_time(1, 2, 0, 5)) is not None


def test_right_justify():
    assert len(lab2.right_justify('test', 90)) == 90
    assert len(re.match(r' *', lab2.right_justify('test', 90)).group(0)) == 86


def test_right_justify_xl():
    assert len(lab2.right_justify('test', 3)) == 4
    assert len(re.match(r' *', lab2.right_justify('test', 3)).group(0)) == 0


def test_center_justify():
    fields = re.match(r'( *)[^ ]( *)', lab2.center_justify('test', 90))
    left_padding = len(fields.groups(1))
    right_padding = len(fields.groups(3))
    assert abs(left_padding - right_padding) < 2


def test_get_square_color():
    assert lab2.get_square_color(1, 1) == 'white'
    assert lab2.get_square_color(4, 4) == 'white'
    assert lab2.get_square_color(7, 7) == 'white'
