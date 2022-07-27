in_list = [1, 1, 2]

print(list(filter(lambda x: in_list.count(x) == 1, in_list)))


# my_list = [x for x in my_list if my_list.count(x) < 2]



# import random
# def fillArrayRandom(size: int) -> list:
#     array = []
#     for i in range(size):
#         array.append(random. randrange(0, 20))
#     return array

# array = fillArrayRandom(int(input("Which size? ")))
# print(array)
# any = [array[i] for i in range(len(array)) if array.count(array[i]) == 1]
# print(any)


# О том, как правильно оформлять путь к файлу (базовый вариант): https://pythonworld.ru/moduli/modul-os-path.html
# https://www.digitalocean.com/community/tutorials/how-to-use-the-pathlib-module-to-manipulate-filesystem-paths-in-python-3-ru

# for row in matrix:
#     for item in row:
#         ''.join('{:4}'.format(item))
#     print('\n')

