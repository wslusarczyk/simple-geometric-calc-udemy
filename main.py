'''Stwórz program, z którego użytkownik może wybrać opcje, aby policzyć powierzchnie figur:
 1)prostokąta
 2)kwadratu
'''


def rectangle(length, width):
    if length == 0 or width == 0:
        return
    else:
        areaRectangle = length * width
        return areaRectangle


def checkRectangleValue(length, width):
    while length == 0 or width == 0:
        print("Your value cannot be zero!")
        length = int(input("Enter the length = "))
        width = int(input("Enter the width = "))
    print("Area of rectangle = ", rectangle(length, width))


def square(lengthSquare):
    if lengthSquare == 0:
        return
    else:
        areaSquare = lengthSquare ** 2
        return areaSquare


def checkSquareValue(lengthSquare):
    while lengthSquare == 0:
        print("Your value cannot be zero!")
        lengthSquare = int(input("Enter the lenghtSquare = "))
    print("Area of square = ", square(lengthSquare))


def userChoice():
    choice = int(input("Choose one \n 1) Rectangle area \n 2) Square area \n 3) Finish \n"))
    return choice


print("A program that calculates the area of a selected figure")

choice = userChoice()

while choice != 3:
    if choice == 1:
        length = int(input("Enter the length = "))
        width = int(input("Enter the width = "))
        checkRectangleValue(length, width)
    elif choice == 2:
        lengthSquare = int(input("Enter the length = "))
        checkSquareValue(lengthSquare)
    elif choice == 3:
        print("Finish")
        exit()
    else:
        print("The given value is not valid! Choose the correct number ")
    choice = userChoice()
