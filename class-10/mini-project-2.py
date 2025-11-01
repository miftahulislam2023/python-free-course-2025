import random # রেন্ডম সংখ্যা তৈরির জন্য ইম্পোর্ট করা হলো pseudorandom number
# কম্পিউটার ১ থেকে ২০ এর মধ্যে একটি সংখ্যা ঠিক করলো
x = random.randint(1, 20)
# print("আমি ১ থেকে ২০ এর মধ্যে একটি সংখ্যা ভেবেছি।")
# print("দেখি আপনি কয়বারে তা ধরতে পারেন!")

attemptLeft = 3
i = 0
isWon = False
while i < attemptLeft:
    y = int(input('Guess the number:'))
    if y == x:
        isWon = True
        break
    elif y < x:
        print('Too low')
    else:
        print('Too high')
    i+=1

print(f'The number is {x}')
if isWon:
    print('Congratulations!')
else:
    print('You lose! Try again')