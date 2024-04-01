#Python program developed by Brian Sheehan
print("Iteration Algorithm for Fundrasing 5K-Marathon")
#start by initalizing variables
intTag = 1000 #starting tag
fltDonation = 0.00
while True:
    strInput=input("Please enter Q to quit or press [Enter] to continue: ")
    if(strInput.upper() == "Q"):
        break
    else:
        strCategory=input("Enter category (W)alker, (A)thlete, (R)unner, (P)erson: ")
        print("Category =",strCategory)
        strName=input("Enter name : ")
        fltDontation=float(input("Enter docation (min 10$/person) : $"))
        print(f'Thank you for your donation = $(fltDonation:.2f)')

        if(strCategory.upper() == "W"):
           strTag="W"+str(intTag)
        elif(strCategory.upper() == "A"):
            strTag="A"+str(intTag)
        else:
            strTag="P"+str(intTag)

        print("Thank you "+strName+" for contributing at WARP speed. Your tag = ",strTag)
        intTag = intTag+1
        print("Enjoy the 5K!")

print("Program Exit. Goodbye!")
