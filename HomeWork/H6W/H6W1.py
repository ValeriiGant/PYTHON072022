# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.

#     *Пример:*

#     - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def fraction_part_list(list_my: list) -> list:
    return [round(i % 1, 2) for i in list_my if type(i) == float]


new_list = [1.1, 1.2, 3.1, 5, 10.01]
print("Initial list: ", new_list)
new_list_my = fraction_part_list(new_list)
print("Fractional parts list: ", new_list_my)
print("Difference between man and min fractional part =", max(new_list_my) - min(new_list_my))