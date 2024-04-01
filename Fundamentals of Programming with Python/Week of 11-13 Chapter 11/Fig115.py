class Person:
    def __init__(self,first, last):
        self.first = first
        self.last = last

    def FullName(self):
        return self.first+" "+self.last

print("Creating an object from class Person")
person1 = Person("Yancy","Doe")
print("First = "+person1.first)
print("Second = "+person1.last)
print("Full Name = ",person1.FullName())
print("\nModifying an object property")
person1.first = "Jane"
print("First = "+person1.first)
print("Full Name = ",person1.FullName())
print("\nDeleting an object")
del person1
