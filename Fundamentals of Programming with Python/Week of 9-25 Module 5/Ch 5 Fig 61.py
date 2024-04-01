#Python sets
print("Python Sets")
setSports={"Baseball","Soccer","Football"}
print(setSports)
print("Length of set =",len(setSports))
print("To add one item use the add() method\n")
setSports.add("Rugby")
print(setSports)
print("\nTo add multipule items use the add update() method")
setSports.update(["Fishing","Tennis"])
print(setSports)
print("\nTo remove any item use the remove() method with value inside parenthesis")
setSports.remove("Rugby")
print(setSports)
print("\nThe clear() method will yield an empty set")
setSports1={"Baseball","Soccer","Football"}
print("First set =",setSports1)
setSports2={"Rugby","Fishing","Tennis"}
print("Second set =",setSports2)
print("To merge two sets use the union() method")
setSports3=setSports1.union(setSports2)
print("Third set =",setSports3)
