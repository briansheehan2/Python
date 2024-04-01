#python for loop
print("Displaying a for loop with range(4)")
for index in range(4):
    print("Python for loop with a range of a single value. Index = ",index)
print("\nPython for loop with range(1,5)")
for index in range(1,5):
    print("Python for loop with range (1,5). Index = ",index)
intLowerBound = 1
intUpperBound = 10
print("\nDisplaying multiplication tables")
intNumber=int(input("Enter an integer number between 2-10 :"))
print("Printing Multiplication Table = :",intNumber)
for index in range(intLowerBound,intUpperBound+1):
              print(intNumber," X ",index," = ",intNumber*index)
print("Thank you")
