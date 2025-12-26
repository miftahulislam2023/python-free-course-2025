class Student:
    def __init__(self, mark):
        self._mark = mark

    @property
    def mark(self):
        return self._mark

    @mark.setter
    def mark(self, value):
        if value < 0:
            print("নেগেটিভ মার্ক হতে পারে না!")
        else:
            self._mark = value

s = Student(80)
s.mark = -10 # Setter কল হবে এবং এরর মেসেজ দিবে
print(s.mark) # Getter কল হবে (Output: 80)