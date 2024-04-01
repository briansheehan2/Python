#Project developed by Brian Sheehan
class Person:
    def __init__(self,first,last,email,street,city,state,zip):
        self.first=first
        self.last=last
        self.email=email
        self.street=street
        self.city=city
        self.state=state
        self.zip=zip
        
    def FullName(self):
        return self.last+", "+self.first

    def Address(self):
        return self.street+"\n"+self.city+", "+self.state+" "+self.zip

    def toString(self):
        return "\n"+self.first+" "+self.last+"\n"+self.email+"\n"+self.street+"\n"+self.city+", "+self.state+" "+self.zip

class Faculty(Person):
    pass

class Student(Person):
    pass

f1=Faculty("Sam","Espana","espana@htc.edu","","","","")
s1=Student("Brian","Sheehan","sheehan@htc.edu","","","","")
s1.street="123 Cherry St"
s1.city="Minneapolis"
s1.state="MN"
s1.zip="55411"
print("Faculty1 First Name =",f1.first)
print("Faculty1 Last Name =",f1.last)
print("Faculty1 Full Name =",f1.FullName())
print("Faculty1 Detail (toString):",f1.toString())
print("\n")
print("Student1 First Name =",s1.first)
print("Student1 Last Name =",s1.last)
print("Student1 Full Name =",s1.FullName())
print("Student1 Detail (toString):",s1.toString())
