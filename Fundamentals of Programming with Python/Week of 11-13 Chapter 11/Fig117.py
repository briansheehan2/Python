class Person:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    def FullName(self):
        return self.first+" "+self.last

class Faculty(Person):
    pass

class Student(Person):
    pass

print("Creating an object from class person")
person1 = Person("Yancy","Doe")
print("First = "+person1.first)
print("Last = "+person1.last)
print("Full Name = ",person1.FullName())
print("Creating an object from class faculty")
faculty1 = Faculty("Jane","Joe")
print("First = "+faculty1.first)
print("Second = "+faculty1.last)
print("Full Name = ",faculty1.FullName())
print("\nCreating an object from class Student")
student1 = Student("John","doe")
print("First = "+student1.first)
print("Full Name = ",student1.FullName())
