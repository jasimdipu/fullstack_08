# class object blue print

class Student:
    # class properties -> attributes, functions
    # attributes -> variable -> global variable, local variable
    # gloabal variable
    name = ""
    dept = ""
    subject = ""

    # constructor -> global variable initialization
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    # functions
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getUniversityName(self):
        # local variable
        universityName = "Daffodil International University"
        print(universityName)


# create an object
student = Student("tarek", "CSE")
print(student.name)
print(student.dept)

student2 = Student("samir", "BBA")
print(student2.name, student2.dept)

student2.name = "Himel"
print(student2.name)

student2.dept = "SS"

print(student2.dept)

student2.getUniversityName()











