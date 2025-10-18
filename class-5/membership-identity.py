'''
# membership
print('a' in 'Miftah')
print(10 in [1, 2, 3, 4, 5])

#identity
a = [1, 2]
b = [1, 2]
c = a
print(a == b) # আউটপুট: True (মান সমান)
print(a is b) # আউটপুট: False (মেমরিতে দুটি ভিন্ন অবজেক্ট)
print(a is c) # আউটপুট: True (একই অবজেক্ট)
'''
x = 10
y = 10
z = x
print(x == y) #true
print(x is y)