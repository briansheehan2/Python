#Creating a class Person
class Person:
    def __init__ (self, first, last):#Initalizing method (aka constructor)
        self.first = first #attrute
        self.last = last #Attribute

    def FullName (self):#method
        return self.first+" "+self.last
print("Creating an object from class Person")
person1 = Person("John","Doe")#Creating an instance from class person
print("First = "+person1.first)
print("Second = "+person1.last)
print("Full Name = ",person1.FullName())
      
