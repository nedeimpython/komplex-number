import math
import cmath
i = -1
while True:
    operation = input("Введите название операции: ")
    if operation == "конец":
        break
    if operation == "сложение":
        x1 = int(input("Введите действительную часть числа z "))
        y1= int(input("Введите мнимую часть числа z "))
        z1 = x1+y1*i
        print(z1)
        x2 = int(input("Введите действительную часть числа z "))
        y2= int(input("Введите мнимую часть числа z "))
        z2 = x2+y2*i
        print(z2)
        z3 = (x1+x2)+i*(y1+y2)
        print("z1+z2 = ", z3)
    if operation == "вычитание":
        x1 = int(input("Введите действительную часть числа z "))
        y1= int(input("Введите мнимую часть числа z "))
        z1 = x1+y1*i
        print(z1)
        x2 = int(input("Введите действительную часть числа z "))
        y2= int(input("Введите мнимую часть числа z "))
        z2 = x2+y2*i
        print(z2)
        z3 = (x1-x2)+i*(y1-y2)
        print("z1-z2 = ", z3)
    if operation == "умножение":
        x1 = int(input("Введите действительную часть числа z"))
        y1= int(input("Введите мнимую часть числа z "))
        z1 = x1+y1*i
        print(z1)
        x2 = int(input("Введите действительную часть числа z "))
        y2= int(input("Введите мнимую часть числа z "))
        z2 = x2+y2*i
        print(z2)
        z3 = (x1*x2-y1*y2)+(x1*y2+x2*y1)
        print("z1*z2 = ", z3)
    if operation == "деление":
        x1 = int(input("Введите действительную часть числа z "))
        y1= int(input("Введите мнимую часть числа z "))
        z1 = x1+y1*i
        print(z1)
        x2 = int(input("Введите действительную часть числа z "))
        y2= int(input("Введите мнимую часть числа z "))
        z2 = x2+y2*i
        print(z2)
        z3 = ((x1*x2+y1*y2)/(x2**2+y2**2))+i*((x2*y1-x1*y2)/(x2**2+y2**2))
        print("z1/z2 = ", z3)
    if operation == "модуль":
        x1 = int(input("Введите действительную часть числа z "))
        y1= int(input("Введите мнимую часть числа z "))
        z1 = x1+y1*i
        print(z1)
        modul_z1 = (x1**2+y1**2)**0.5
        print("|z| = ",modul_z1)
    if operation == "корень квадратный":
        x1 = int(input("Введите действительную часть числа z "))
        y1= int(input("Введите мнимую часть числа z "))
        z1 = x1+y1*i
        print(z1)
        print("Корень квадратный из комплекснго числа z = ", cmath.sqrt(z1))
        
