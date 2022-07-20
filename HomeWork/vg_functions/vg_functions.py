# Functions for use at work VG.

import random as rnd
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

def rnd_int_list_n_minus_n(digit: int) -> list:
    list = []

    for i in range(0, digit):
        list.append(rnd.randint(-digit, digit+1))

    return list
# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

def rnd_float_list_n_minus_n(digit: int) -> list:
    list = []

    for i in range(0, digit):
        list.append(round(rnd.randint(-digit, digit+1) + rnd.random(), 2))

    return list

# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

def sum_indices_list(list: list) ->int: #сумма элементов/индексов в списке
    sum = 0

    for i in list:
        sum+=i

    return sum

# vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv