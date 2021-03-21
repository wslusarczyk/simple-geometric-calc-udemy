'''Stwórz program, z którego użytkownik może wybrać opcje, aby policzyć powierzchnie figur:
 1)prostokąta
 2)kwadratu
'''

def rectangle(lenght,width):
    if lenght == 0 or width == 0:
        return
    else:
        areaRectangle = lenght * width
        return areaRectangle

def checkRectangleValue(lenght, width):
    while lenght == 0 or width == 0:
        print("Your value cannot be zero!")
        lenght = int(input("Enter the lenght = "))
        width = int(input("Enter the width = "))
    print("Area rectangle = ", rectangle(lenght,width))

def square(lenghtSquare):
    if lenghtSquare == 0:
        return
    else:
        areaSquare = lenghtSquare**2
        return areaSquare

def checkSquareValue(lenghtSquare):
    while lenghtSquare == 0:
        print("Your value cannot be zero!")
        lenghtSquare = int(input("Enter the lenghtSquare = "))
    print("Area rectangle = ", square(lenghtSquare))

print("A program that counts the area of a selected figure")

def userChoise():
    choise = int(input("Choise one option \n 1) Rectangle area \n 2) Square area \n 3) Finish \n"))
    return choise

choise = int(input("Choise one option \n 1) Rectangle area \n 2) Square area \n 3) Finish \n"))

'''while choise != 1 and choise != 2 and choise !=3:
    choise = int(input("Choise one option \n 1) Rectangle area \n 2) Square area \n 3) Finish \n"))'''
while choise !=3:
    if choise == 1:
        lenght = int(input("Enter the lenght = "))
        width = int(input("Enter the width = "))
        checkRectangleValue(lenght, width)
    elif choise == 2:
        lenghtSquare = int(input("Enter the lenght = "))
        checkSquareValue(lenghtSquare)
    elif choise == 3:
        print("Finish")
    else:
        print("The given value is not valid! Choose the correct number ")
    choise = int(input("Choise one option \n 1) Rectangle area \n 2) Square area \n 3) Finish \n"))
