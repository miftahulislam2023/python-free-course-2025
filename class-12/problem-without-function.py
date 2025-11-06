'''
1. Repetaion of code -> কোডের পুনরাবৃত্তি -> Loop use করে সলভ করা

'''
celcius = float(input('Enter temperature:'))
farenheit = celcius * 9 / 5 + 32
print(farenheit)

x = 2
square =  x**2
print(square)

# নিশ্চায়ক ax^2+bx+c=0, b^2-4ac

# Problem 2: Sum of numbers from 1 to n
n = int(input('Enter a number: '))
sum = 0
for i in range(1, n+1):
    sum += i
print(f'Sum from 1 to {n} is {sum}')

# Problem 3: Factorial calculation
num = int(input('Enter a number: '))
factorial = 1
for i in range(1, num+1):
    factorial *= i
print(f'Factorial of {num} is {factorial}')

# Problem 4: Fibonacci sequence up to n terms
terms = int(input('Enter number of terms: '))
a, b = 0, 1
print('Fibonacci sequence:')
for i in range(terms):
    print(a, end=' ')
    a, b = b, a + b
print()

# Problem 5: Check if a number is prime
num = int(input('Enter a number: '))
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')

# Problem 6: Reverse a string
text = input('Enter a string: ')
reversed_text = ''
for char in text:
    reversed_text = char + reversed_text
print(f'Reversed string: {reversed_text}')

# Problem 7: Count vowels in a string
text = input('Enter a string: ')
vowels = 'aeiouAEIOU'
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f'Number of vowels: {count}')

# Problem 8: Simple interest calculation
principal = float(input('Enter principal amount: '))
rate = float(input('Enter rate of interest: '))
time = float(input('Enter time in years: '))
simple_interest = (principal * rate * time) / 100
print(f'Simple interest: {simple_interest}')

# Problem 9: Area of rectangle
length = float(input('Enter length: '))
width = float(input('Enter width: '))
area = length * width
print(f'Area of rectangle: {area}')

# Problem 10: Grade calculator
marks = float(input('Enter marks: '))
if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
elif marks >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f'Grade: {grade}')

# Problem 11: Number guessing game
import random
secret_number = random.randint(1, 100)
guess = 0
attempts = 0
while guess != secret_number:
    guess = int(input('Guess a number between 1 and 100: '))
    attempts += 1
    if guess < secret_number:
        print('Too low!')
    elif guess > secret_number:
        print('Too high!')
    else:
        print(f'Congratulations! You guessed it in {attempts} attempts.')