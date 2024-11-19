from .. import lab4
import random


random.seed()

def test_min():
    assert lab4.min([1, 2, 3]) == 1
    assert lab4.min([3, 2, 1]) == 1
    assert lab4.min([28, 25, 42, 2, 28]) == 2
    assert lab4.min([1]) == 1
    try:
        lab4.min([])
    except ValueError:
        assert True
    else:
        assert False


def test_max():
    assert lab4.max([1, 2, 3]) == 3
    assert lab4.max([3, 2, 1]) == 3
    assert lab4.max([28, 25, 42, 2, 28]) == 42
    assert lab4.max([1]) == 1
    try:
        lab4.max([])
    except ValueError:
        assert True
    else:
        assert False



def test_average():
    assert lab4.average([1, 2, 3]) == 2
    assert lab4.average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
    assert lab4.average([12, 20, 37]) == 23
    assert lab4.average([0, 0, 0, 0, 0]) == 0
    testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    for i in range(1000):
        random.shuffle(testData)
        assert lab4.average(testData) == 2


def test_median():
    try:
        lab4.median([])
    except ValueError:
        assert True
    else:
        assert False
    assert lab4.median([1, 2, 3]) == 2
    assert lab4.median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
    assert lab4.median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6
    testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
    for i in range(1000):
        random.shuffle(testData)
        assert lab4.median(testData) == 6


def test_mode():
    try:
        lab4.mode([])
    except ValueError:
        assert True
    else:
        assert False
    assert lab4.mode([1, 2, 3, 4, 4]) == (4,)
    assert lab4.mode([1, 1, 2, 3, 4]) == (1,)
    testData = [1, 2, 3, 4, 4]
    for i in range(1000):
        random.shuffle(testData)
        assert lab4.mode(testData) == (4,)

        
def test_roll_dice():
    for d in (4, 6, 8, 10, 12, 20):
        for num in range(1, 9):
            for trials in range(10):
                roll = lab4.roll_dice(num, d)
                assert len(roll) == num
                for die in roll:
                    assert 1 <= die <= d
