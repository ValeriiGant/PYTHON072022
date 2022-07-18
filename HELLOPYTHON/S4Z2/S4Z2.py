# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами: 
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python
path = 'HELLOPYTHON/file.txt'
# with open(path, 'r') as my_file:
#     data = my_file.read()

# data = data.split()
# print(data)
# data = data[:-2]
# print(data)
# data = [int(data[0][:-3]), int((data[1] + data[2])[:-1]), int(data[3] + data[4])]
# print(data)
# # D=b^2-4ac
# d = data[1]**2 - 4 * data[0] * data[2]
# print(d)
# # x=((-b(+-))(d^(1/2)))/(2*a))
# x_1 = (-data[1] + d**0.5) / (2 * data[0])
# x_2 = (-data[1] - d**0.5) / (2 * data[0])
# print(x_1, x_2)



with open(path, 'r') as f:
    a = int(f.readline())
    b = int(f.readline())
    c = int(f.readline())

disc = b**2 - 4 * a * c
x1 = -b + (disc**(1/2) / (2 * a))
x2 = -b - (disc**(1/2) / (2 * a))
print(x1, x2)

with open(path, 'a') as f:
    f.write(f'\n Корень 1: {x1}')
    f.write(f'\n Корень 2: {x2}')




# import os

# def is_int(str: str) -> bool:
#     try:
#         int(str)
#         return True
#     except ValueError:
#         return False


# def input_list_int_numbers(str_in: str) -> list:
#     list_dirty = str_in
#     list_clean = []
#     for elem in list_dirty:
#         if is_int(elem):
#             list_clean.append(int(elem))
#     return list_clean


# path = r'folder\disk.txt'

# with open(path, 'r') as d:
#     list = d.read().split("\n")
#     print(list)

# list2 = input_list_int_numbers(list)
# print(list2)

# d = list2[1]**2 - 4* list2[0] * list2[2]
# print(d)

# with open(path, 'a') as f:

