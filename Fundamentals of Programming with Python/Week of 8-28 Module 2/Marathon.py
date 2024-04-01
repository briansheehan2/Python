#Python program developed by Brian Sheehan - Partial program to complete in class
print("Iteration Algoritm for Fundraising 5K-Marathon")
#Start by initalizing variables (placeholders for values used in the program)
intTag = 1000 #Starting number for tag
fitDontation = 0.00
while True:
    strInput = input("Please enter Q to quit or press [Enter] to continue") #Get Input
    if (strInput.upper() == "Q"):   #Outer if/else
        break
    else:
        strCategory = input("Enter category (W)alker, (A)thlete, (R)unner, (P)erson:") #Get Input
        print("Category =",strCategory)
        strName = input("Enter name:")
        fitDontation = float(input("Enter dontation (minimum $10/person):$")) #Get Input
        #(fitdonation:.2f) = It formats the output to two decimals
        print(f"Thank you for your donation = $(fitDonation:.2f)") #Processing donation

        if(strCategory.upper() == "W"): #Processing category
            strTag = "W"+str(intTag)
        elif(strCategory.upper() == "A"): #Inner if/elf/else
            strTag = "A"+str(intTag)
        else:
            strTag = "P"+str(intTag)
        #Final Output
        print("Thank you "+strName+" for contributing at WARP speed. Your tag = ",strTag)
        intTag = intTag +1
        print("Enjoy the 5K-Marathon!")

#Stop by saying goodbye
print("Program Exit. Goodbye!")

        
        
