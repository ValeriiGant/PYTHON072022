# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции вводит пользователь через пробел.

def fill_array(num):
    array=[]
    for i in range(-num, num+1):
        array.append(i)
    return array


def multiplex(arr, indices: str):
    j, k = map(int, indices.split(" ")) #Метод split() разбивает строку по указанному разделителю и возвращает список строк.
    print(f"Произведение указанных элементов (индексов)= {arr[j]*arr[k]}")


n = int(input("Введите количество элементов N = "))
arr = fill_array(n)
print(arr)

multiplex(arr, input(f"Введите два числа от 0 до {n*2} через пробел: "))