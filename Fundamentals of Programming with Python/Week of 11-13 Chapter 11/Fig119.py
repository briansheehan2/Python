class Person:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    def FullName(self):
        return self.first+" "+self.last

class Faculty(Person):
    def __init__(self,first,last,department):
        super().__init__(first, last)
        self.department = department

class Student(Person):
    pass

print("Creating an object from class person")
person1 = Person("Brian","Sheehan")
print("First Name = "+person1.first)
print("Second Name = "+person1.last)
print("Full Name = ",person1.FullName())
print("\nCreating an object from class Faculty")
faculty1 = Faculty("Jane","Doe","Math")
print("First Name = "+faculty1.first)
print("Full Name= ",faculty1.FullName())
print("Dept = ",faculty1.department)
