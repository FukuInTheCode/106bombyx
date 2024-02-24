import sys


from src.case1 import do_case1
from src.case2 import do_case2


def is_between_one_and_four(number):
    if 1 <= number <= 4:
        return True
    else:
        return False


def is_int(num):
    try:
        int(num)
        return True
    except ValueError:
        return False


def is_float(num):
    try:
        float(num)
        return True
    except ValueError:
        return False


def check_arg(abrs: list[str]) -> int:
    if len(abrs) == 2:
        if is_float(abrs[0]) and is_float(abrs[1]) and float(abrs[0]) >= 0 and is_between_one_and_four(float(abrs[1])):
            do_case1(float(abrs[0]), float(abrs[1]))
            return 0
        sys.exit(84)
    if len(abrs) == 3:
        if is_float(abrs[0]) and is_int(abrs[1]) and is_int(abrs[2]) and float(abrs[0]) >= 0 and int(abrs[1]) > 0 and int(abrs[2]) > 0 and int(abrs[2]) > int(abrs[1]) > 0:
            do_case2(float(abrs[0]), int(abrs[1]), int(abrs[2]))
            return 0
        return 84
    return 84
