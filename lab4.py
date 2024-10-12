"""Lab 4
Module implementing very basic statistics and probability functions.

Completed by Matthew Butler on 2024-09-30 for DS-1043"""

Number = int | float
Sequence = list[int] | list[float] | tuple[int] | tuple[float]


def min(numbers: Sequence) -> Number:
    if len(numbers) < 1:
        raise ValueError("min() argument is empty")
    min_value = numbers[0]
    for value in numbers:
        if min_value > value:
            min_value = value
    return min_value


def max(numbers: Sequence) -> Number:
    if len(numbers) < 1:
        raise ValueError
    max_value = numbers[0]
    for value in numbers:
        if max_value < value:
            max_value = value
    return max_value


def sum(numbers: Sequence) -> Number:
    if len(numbers) < 1:
        raise ValueError
    answer: Number = 0
    for number in numbers:
        answer = answer + number
    return answer


def average(numbers: Sequence) -> Number:
    if len(numbers) < 1:
        raise ValueError
    total = sum(numbers)
    return total / len(numbers)


def median(numbers: Sequence) -> Number:
    """Returns the mid-point value of the given data in numbers"""
    if len(numbers) < 1:
        raise ValueError
    index = len(numbers) // 2
    numbers.sort()
    if len(numbers) % 2 == 1:
        return numbers[index]
    else:
        return average((numbers[index], numbers[index - 1]))


def mode(numbers: Sequence) -> tuple[Number, ...]:
    """Returns a tuple of the most frequently appearing members of numbers"""
    if len(numbers) < 1:
        raise ValueError
    counter: dict[Number, int] = {}
    for number in numbers:
        if number in counter.keys():
            counter[number] = counter[number] + 1
        else:
            counter[number] = 1
    sorted_numbers = sorted(numbers, key=lambda x: counter[x])
    mode_count = counter[sorted_numbers[0]]
    mode = ()
    for number in sorted_numbers:
        if counter[number] < mode_count:
            break
        mode = mode + (number,)
    return mode
