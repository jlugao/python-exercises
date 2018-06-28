from functools import reduce



def is_happy_list(numbers: list) -> list:
    return list(map(is_happy,numbers))


def is_happy(number: int) -> bool:
    result=number
    for i in range(100):
        digits = [int(digit) for digit in str(result)]
        result = sum(map(lambda x:x**2, digits))
        if result == 1:
            return True
        if result == number:
            return False
    return False