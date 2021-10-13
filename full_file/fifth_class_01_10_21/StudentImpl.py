from student import Student


class StudentImpl(Student):

    def __init__(self, name, dept):
        self.name = name
        self.dept = dept


    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getDept(self):
        return self.dept

    def setDept(self, dept):
        self.dept = dept


# student Implementation class object
student = StudentImpl("Tarek", "IT")
print(student.name, student.dept)
print(student.getName())
print(student.getDept())
