from re import I


a = "Hello World"
b =1.23
c =123
print(c) #вывод строки
print(a,"-",b,"-",-c) #интерполяция
print ("{2}-{0}-{1}".format (a,b,c)) #формат
print (f'{a}-{b}-{c}')
#print ("Введите d=")
#d=int (input())
#print ("Введите e=")
#e=float (input()) #вещественное 
g=3
i=3
k=1.234569
j1=g+i 
j2=g-i
j3=g*i
j4=g/i
j5=g//i
j6=g%i
j7=g**i# возведение в степень
j8=round (g*k,3) #округление до 3 знаков
g+=6 #g=g+6
print(j1,j2,j3,j4,j5,j6,j7,j8,g)
if g>k:
    print (g)
else:
    print (k)    