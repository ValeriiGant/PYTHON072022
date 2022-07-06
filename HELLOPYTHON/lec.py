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
#username = input ("Введите имя = ")
#if username == "Сергей":
 #   print ("Ура, это же Сергей!")
#elif username == "Ильнар":             #логический оператор
  #  print ("Ух ты, это же Ильнар!")
#else:
    #print ("Привет, ",username,"!")  

original = 23 # ЦИКЛЫ !!!
inverted = 0
while original !=0: #не равно 0 !=0
     inverted=inverted*10+(original % 10)
     original//=10
     print(original)
else:
    print ("Пожалуй")
    print ("хватит )")
print(inverted)
#Управляющие конструкции
#for
for i in range (1, 10, 2):
    print(i**2)
# help (int)

def f (x):
    if x==1:
        return "Целое"
    elif x==2.3:
        return 23
    else:
        return
arg =1
print(f(arg))
print(type(f(arg)))
