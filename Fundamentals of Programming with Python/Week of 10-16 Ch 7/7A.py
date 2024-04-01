import math


def udfMenuOptions():
    print("********************")
    print("Python User-Defined Functions (udf) Demo")
    print("********************")
    print("1. Calculate the Circumference (C) of a circle (C= 2 * pi * radius)")
    print("2. Calculate the Area (A) of a circle (A = pi * radius")
    print("3. Calculate area of a rectangle")
    print("4. Calculate area of a Triangle")
    print("5. Calculate area of a square")
    print("0. Enter Digit (1-5) to select a menu option or 0 to quit \n")
    return None

def main():
    while True:
        udfMenuOptions()
        menuChoice=int(input("Enter Menu Selection Number: "))
        if (menuChoice == 0):
            print("Have a nice day.")
            break
        elif (menuChoice == 1):
            print("Calculating the circumfrance of a Circle")
            fltRadius=float(input("Enter Radius of the circle: "))
            fltCircumfrance = udfCircumfrance(fltRadius)
            print("Circumfrance = ",fltCircumfrance)
        else:
            print("Invalid Selection. To quit, please enter 0")

def udfCircumfrance(radius):
    return 2*radius*math.pi

if __name__ == "__main__":
    main()
                            
