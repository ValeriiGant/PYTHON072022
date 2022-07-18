#Реализуйте алгоритм перемешивания списка.
import random
n = int(input("Введите число элементов в списке: "))
arr = [random.randint(-100,100) for i in range(n)] #Метод .randint Возвращает случайное число в пределах заданного промежутка
print(arr)

def mix(arr):
    l = len(arr)
    indices = []     #создаем индекс (массив) указанного списка
    new_arr = []
    i = 0
    while(i<l):                    
        j = random.randint(0, l-1) 
        if j not in indices:
            indices.append(j)    
            new_arr.append(arr[j]) 
            i += 1
    return new_arr
print(mix(arr))