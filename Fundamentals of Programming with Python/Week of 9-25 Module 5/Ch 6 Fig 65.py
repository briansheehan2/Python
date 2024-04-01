##Python IF/ELIF/ELSE
intAge=int(input("Enter patients age : "))
print("Simple if/else statement")
if(intAge >= 18):
    print("Patient is an adult. Preform exam")
else:
    print("Patient is a minor. Do not preform exam")
    print("\nSimple IF/ELIF/ELSE statement")
    blnGuardian=True
    if(intAge >= 18):
        print("Patient is an adult. Preform exam")
    elif(blnGuardian == True):
        print("Patient is a minor. Preform exam with guardian")
    else:
        print("Do not preform exam. Have patient return with guardian")
        
