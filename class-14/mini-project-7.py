import random
def roll_dice():
    # ছক্কার মান ১ থেকে ৬ এর মধ্যে হয়
    roll_result = random.randint(1, 6)
    print(f"🎲 You rolled a: {roll_result}")

# সিমুলেশন
print("--- Dice Rolling Simulator ---")
while True:
    user_input = input("Press Enter to roll the dice (or 'q' to quit): ")    
    if user_input.lower() == 'q':
        print("Thanks for playing!")
        break
    roll_dice()