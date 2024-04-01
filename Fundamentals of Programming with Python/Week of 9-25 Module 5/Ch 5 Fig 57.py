dictStudent1={"ID#":"69","name":"Brian","email":"briguy1660@aol.com","major":"Software Development"}
print("Printing the length of the dictionary")
print("length =",len(dictStudent1))
print("Printing Student1 dictionary\n")
print(dictStudent1)
print("Changing the value of a key")
dictStudent1["email"]="briansheehan2@gmail.com"
print("Printing Student1 dictionary\n")
print(dictStudent1)
print("\nPrinting the value (Brian) of a key (name)\n")
print(dictStudent1.get("name"))

print("\nPrinting all keys in the dictionary\n")
for key in dictStudent1:
    print(key)

print("\nPrinting all values in the dictionary\n")
for value in dictStudent1.values():
    print(value)

print("\nPrinting all key-value pairs in the dictionary\n")
for key, value in dictStudent1.items():
    print(key,value)
    
dictStudent2={"ID#":"80085","name":"Molly","email":"mollyrox@gmail.com","major":"being hot"}
print("\nPrinting Student2 dictionary\n")
print(dictStudent2)

print("\nAdding a key-value pair (phone)\n")
dictStudent2["phone"]="612-991-4593"
print(dictStudent2)

print("\nRemoving an exisiting item (Email)\n")
dictStudent2.pop("email")
print(dictStudent2)

dictClass={"Student1":dictStudent1,"Student2":dictStudent2}
print("\nPrinting nested dictionary (Student1, Student2) \n")
print(dictClass)

print("\nBrian Test\n")
print("Brian test\n")

for key, value in dictClass.items():
    print(key,value)
