def input_num()->int:
    a=str()
    while not a.isdigit():
        a=(input("Введите число:"))
        if a.isdigit():
            return int (a)
        else:
            print ("Введено не число!")


def input_operation()-> str:
    a=str()
    while a != "+" or a != "*" or a != "/":
        a=str(input ("Введите число"))
