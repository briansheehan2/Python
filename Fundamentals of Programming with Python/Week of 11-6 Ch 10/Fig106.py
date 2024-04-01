class Person:
    def __init__ (self, first, last):
        self.first = first
        self.last = last

    def FullName(self):
        return self.first+" "+self.last

print("Creating an object from class Person")
person1 = Person("John","Doe")
print("First = "+person1.first)
