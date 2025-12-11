class Student:
    totalStudents = 100
    def __init__(self, phoneNumber):
        self.phoneNumber = phoneNumber

print(Student.totalStudents)
s1 = Student('01512312')
print(s1.phoneNumber)
s2 = Student('010231')
print(s2.phoneNumber)
print(s1.totalStudents)
print(s2.totalStudents)