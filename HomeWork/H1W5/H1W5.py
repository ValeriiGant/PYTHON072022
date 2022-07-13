# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
import math

def coord(text): 
    list = []
    list.append(int(input(f"Введи координаты Х {text} : ")))
    list.append(int(input(f"Введи координаты Y {text} : ")))
    return list

print("Введите точки координат:")
first_point  = coord("(первая точка)")
second_point = coord("(вторая точка)")

result = math.sqrt((first_point[0] - second_point[0])**2 + (first_point[1] - second_point[1])**2)

print(f"Расстояние между двумя точками = {round (result,2)}")