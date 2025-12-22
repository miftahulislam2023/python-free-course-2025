class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def showInfo(self):
        print(self.name, self.email, sep=': ')

# u1 = User('Miftahul Islam', 'miftah@miftahcoding.com')
# u2 = User('Atik Shahriar', 'suvo@miftahcoding.com')

# u1.showInfo()
# u2.showInfo()

class Admin(User):
    def __init__(self, name, email, auth):
        super().__init__(name, email)
        self.auth = auth
    def changeSettings(self):
        print('Changed settings successfully')
        
    def showInfo(self):
        print(self.name, ': ', self.email)
        print('Auth: ', self.auth)


adm1 = Admin('Miftahul Islam', 'miftah@miftahcoding.com', 'Google Authenticator')
adm1.showInfo()
adm1.changeSettings()

class Student(User):
    def takeExam(self):
        print('Exam taken successfully')

s1 = Student('Abdullah', 'abdullah@gmail.com')
s1.showInfo()
s1.takeExam()
# s1.changeSettings()

class Teacher(User):
    def setExam(self):
        print('Exam set successfully')

t1 = Teacher('Iftekhar', 'iftekhar@protonmail.com')
t1.showInfo()
t1.setExam()
