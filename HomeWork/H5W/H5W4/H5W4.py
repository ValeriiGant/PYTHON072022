# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
import os

def x_to_rle():
    path ="HomeWork\H5W\H5W4" + os.sep + "h5w4.txt"
    with open("HomeWork\H5W\H5W4\h5w4.txt", "r") as my_file:
        x = my_file.readline()
        xc = x[0]
        x_rle = ""
        count = 1
        for i in range(1, len(x)):
            if x[i] == xc[-1]:
                count += 1
            else:
                x_rle += str(count) + xc[-1]
                xc += x[i]
                count = 1
        x_rle += str(count) + xc[-1]

    path ="HomeWork\H5W\H5W4" + os.sep + "h5w4_rle.txt"
    with open(path, "w") as my_file:   
        my_file.write(x_rle)


def rle_to_x():
    path ="HomeWork\H5W\H5W4" + os.sep + "h5w4_rle.txt"
    with open(path, "r") as my_file:
        x_rle = my_file.readline()
        x =""
        count = ""
        for i in range(len(x_rle)):
            if x_rle[i].isdigit(): count += x_rle[i]
            else:
                x += int(count) * x_rle[i]
                count = ""

    path ="HomeWork\H5W\H5W4" + os.sep + "new_h5w4.txt"
    with open(path, "w") as my_file:   
        my_file.write(x)

x_to_rle()
rle_to_x()