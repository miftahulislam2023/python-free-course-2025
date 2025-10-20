# Namota
try:
 x = int(input('Enter a number: '))
 tenX = x * 10
 temp = x
 while x <= tenX:
     print(x)
     x += temp
except ValueError:
   print('Exiting....Invalid number!')