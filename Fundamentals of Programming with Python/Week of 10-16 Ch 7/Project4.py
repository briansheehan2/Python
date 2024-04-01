import math
#website

def udfMenuOptions():
    print("********************")
    print("1. Calculate the circunference of a circle. Circunference = 2*radius*pi")
    print("2. Calculate the area of a circle. Area = radius*radius*pi")
    print("0. To quit")

def main():
    while True:
        udfMenuOptions()
        menuChoice=int(input("Enter menu option number : "))
        if (menuChoice == 0):
            print("Program developed by Brian Sheehan")
            break
        elif (menuChoice == 1):
            print("Calculating circunference")
            fltRadius = float(input("Enter radius :"))
            fltCircunference = udfCircunference(fltRadius)
            print("Circunfrence = ",format(fltCircunference, '.2f'))
        elif (menuChoice == 2):
            print("Calculating area of circle")
            fltRadius = float(input("Enter radius :"))
            fltCircleArea=udfCircleArea(fltRadius)
            print("Area of circle = ",format(fltCircleArea,'.2f'))
        else:
            print("Invalid option. Try again!")

def udfCircleArea(radius):
    print("The math.pi value =",math.pi)
    return pow(radius,2)*math.pi

def udfCircunference(radius):
    print("The math.pi value =",math.pi)
    return 2*radius*math.pi

main()

