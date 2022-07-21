# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def decimal_to_binary(digit):        
    if digit == 0 or digit == 1:
        return str(digit)
    return str(digit % 2) + decimal_to_binary(digit // 2) # деление на 2


def solution(digit):       
    return int((decimal_to_binary(digit))[::-1])


digit = int(input("\n Введите десятичное число: "))
print(f"\n Решение: десятичное число {digit} в двоичной системе: {decimal_to_binary(digit)}\n")