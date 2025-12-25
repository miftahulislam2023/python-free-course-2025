class Magic:
    def __str__(self):
        return 'This is a str dunder method'
    def __len__(self):
        # print(23)
        return 23
    # def __add__(self):

m = Magic()
print(len(m))