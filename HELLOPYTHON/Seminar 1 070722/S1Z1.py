#Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.
a = int(input('Введите первое число: '))
b = int(input('Введите второе чисоло: '))
if b == a ** 2:
    print(f'Число {b} является квадратом числа {a}!')
elif a == b ** 2:
    print(f'Число {a} является квадратом числа {b}!')
else:
    print(f'Число {b} не является квадратом числа {a}!')