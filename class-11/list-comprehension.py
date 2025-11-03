# squares_comp = [i * i for i in range(1, 11)]
list1 = [1,2,3,4,5,6,7,8,9,10]
for i in range(11, 101):
    list1.append(i)
# print(list1)

# যে expression/প্যাটার্ন use করতে চাচ্ছেন তা লিখব
list2 = [x for x in range(1, 101)]
list3 = [x**3 for x in range(1, 11, 2)]
print(list3)