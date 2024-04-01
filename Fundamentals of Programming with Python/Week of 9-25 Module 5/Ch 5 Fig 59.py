#Python lists
print("Python Lists")
lstCountries=["Canada","USA","Mexico","Guatemala","Belize"]
print("Printing the length of the list =",len(lstCountries))
print("Printing the list of countries")
print(lstCountries)
print("Printing the first item of the list (left to right)")
print(lstCountries[0])
print("Printing the second item of the list (L to R)")
print(lstCountries[1])
print("Printing the last item of list (R to L)")
print(lstCountries[-1])
print("\nbriantest-\n")
print(lstCountries[3])
print("\nendbriantest\n")

print("\nThe append() method is used to add items at the end of the list")
lstCountries.append("El Salvador")
print(lstCountries)
print("\nTo remove an item use the remove() method with a value in the parenthesies")
lstCountries.remove("Belize")
print(lstCountries)
print("\nUse the pop() method to remove the last item or specify an index")
lstCountries.pop()
print(lstCountries)
lstCountries.pop(2)
print(lstCountries)
lstCountries.insert(3,"ZEBULON")
print(lstCountries)
lstCountries.pop(3)
lstCountries.insert(1,"zebulon")
print(lstCountries)
