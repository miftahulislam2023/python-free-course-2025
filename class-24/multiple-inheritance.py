class Father:
    def gardening(self):
        print("বাবার বাগান করার শখ আছে।")

class Mother:
    def cooking(self):
        print("মা খুব ভালো রান্না করেন।")

class Child(Father, Mother):
    def sports(self):
        print("সন্তান খেলাধুলা পছন্দ করে।")

# অবজেক্ট তৈরি
c = Child()

c.gardening() # বাবার মেথড কল হবে
c.cooking()   # মায়ের মেথড কল হবে
c.sports()    # নিজের মেথড কল হবে