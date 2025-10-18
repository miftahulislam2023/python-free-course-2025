# এমন একটা প্রোগ্রাম লিখ যা মার্ক অনুযায়ী গ্রেড প্রিন্ট করবে
'''
A+ >= 80
A >= 70 and <= 79
A- >= 60 and <= 69
B >= 50 and <= 59
C >= 40 and <= 49
D >= 33 and <= 39
'''
# mark = 85
# if mark >= 80 and mark <= 100:
#     print('A+')
# elif mark >= 70 and mark < 80:
#     print('A')
# elif mark >= 60 and mark < 70:
#     print('A-')
# elif mark >= 50 and mark < 60:
#     print('B')
# elif mark >= 40 and mark < 50:
#     print('C')
# elif mark >= 33 and mark < 40:
#     print('D')
# elif mark < 33 and mark >= 0:
#     print('Fail')
# elif mark < 0 or mark > 100:
#     print('Invalid mark')

'''
mark = 105
if mark >= 80 and mark <= 100:
    print('A+')
elif mark >= 70 and mark < 80:
    print('A')
elif mark >= 60 and mark < 70:
    print('A-')
elif mark >= 50 and mark < 60:
    print('B')
elif mark >= 40 and mark < 50:
    print('C')
elif mark >= 33 and mark < 40:
    print('D')
elif mark < 33 and mark >= 0:
    print('Fail')
else:
    print('Invalid mark')

print('Program completed!')
'''

age = float(input("আপনার বয়স কত? "))
if age < 13:
    print("আপনি একজন শিশু।")
elif age >= 13 and age < 18:
    print("আপনি একজন কিশোর।")
elif age >= 18 and age < 60:
    print("আপনি একজন প্রাপ্তবয়স্ক।")
else:
    print("আপনি একজন মুরুব্বি। আপনি কম্পিউটারে কী করেন?")