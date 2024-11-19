from .. import lab3
import time


def test_is_odd():
    assert lab3.is_odd(42) is False
    assert lab3.is_odd(9999) is True
    assert lab3.is_odd(-10) is False
    assert lab3.is_odd(-11) is True
    assert lab3.is_odd(3.1415) is False


def test_is_even():
    assert lab3.is_even(42) is True
    assert lab3.is_even(9999) is False
    assert lab3.is_even(-10) is True
    assert lab3.is_even(-11) is False
    assert lab3.is_even(2.7182) is False


def test_time_elapsed():
    assert lab3.time_elapsed(round(time.time())) == (0, 0, 0, 0)
    assert lab3.time_elapsed(round(time.time()) - 1) == (0, 0, 0, 1)
    assert lab3.time_elapsed(round(time.time()) - 60) == (0, 0, 1, 0)
    assert lab3.time_elapsed(round(time.time()) - 60 * 60) == (0, 1, 0, 0)
    assert lab3.time_elapsed(round(time.time()) - 24 * 60 * 60) == (1, 0, 0, 0)
    assert lab3.time_elapsed(round(time.time()) - (24 * 60 * 60 + 60 * 60 + 60 + 1)) == (1, 1, 1, 1)


def test_area():
    assert lab3.area(10, 10) == 100
    assert lab3.area(0, 9999) == 0
    assert lab3.area(5, 8) == 40


def test_perimeter():
    assert lab3.perimeter(10, 10) == 40
    assert lab3.perimeter(0, 9999) == 19998
    assert lab3.perimeter(5, 8) == 26


def test_volume():
    assert lab3.volume(10, 10, 10) == 1000
    assert lab3.volume(9999, 0, 9999) == 0
    assert lab3.volume(5, 8, 10) == 400


def test_surface_area():
    assert lab3.surface_area(10, 10, 10) == 600
    assert lab3.surface_area(9999, 0, 9999) == 199960002
    assert lab3.surface_area(5, 8, 10) == 340


def test_get_square_color():
    assert lab3.get_square_color(1, 1) == 'white'
    assert lab3.get_square_color(4, 4) == 'white'
    assert lab3.get_square_color(7, 7) == 'white'
    assert lab3.get_square_color(2, 1) == 'black'
    assert lab3.get_square_color(1, 2) == 'black'
    assert lab3.get_square_color(0, 8) == ''
    assert lab3.get_square_color(2, 9) == ''


def test_prettify_time():
    assert lab3.prettify_time(0, 0, 0, 0) == ''
    assert lab3.prettify_time(1, 0, 0, 0) == '1 day'
    assert lab3.prettify_time(0, 1, 0, 0) == '1 hour'
    assert lab3.prettify_time(0, 0, 1, 0) == '1 minute'
    assert lab3.prettify_time(0, 0, 0, 1) == '1 second'
    assert lab3.prettify_time(1, 2, 0, 5) == '1 day, 2 hours, 5 seconds'


def test_right_justify():
    assert lab3.right_justify('test', 20) == '                test'
    assert lab3.right_justify('test', 3) == 'test'


def test_center_justify():
    test_value = lab3.center_justify('test', 20)
    assert test_value == '        test' or test_value == '        test        '


def test_fizz_buzz():
    no_space = '1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz'
    with_space = '1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz Fizz 22 23 Fizz Buzz 26 Fizz 28 29 FizzBuzz 31 32 Fizz 34 Buzz '
    assert lab3.fizz_buzz(35) == no_space or lab3.fizz_buzz(35) == with_space


def test_ordinal_suffix():
    assert lab3.ordinal_suffix(0) == '0th'
    assert lab3.ordinal_suffix(1) == '1st'
    assert lab3.ordinal_suffix(2) == '2nd'
    assert lab3.ordinal_suffix(3) == '3rd'
    assert lab3.ordinal_suffix(4) == '4th'
    assert lab3.ordinal_suffix(10) == '10th'
    assert lab3.ordinal_suffix(11) == '11th'
    assert lab3.ordinal_suffix(12) == '12th'
    assert lab3.ordinal_suffix(13) == '13th'
    assert lab3.ordinal_suffix(14) == '14th'
    assert lab3.ordinal_suffix(101) == '101st'
