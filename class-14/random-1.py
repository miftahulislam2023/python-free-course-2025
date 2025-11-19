import random

# ১ থেকে ১০ এর মধ্যে একটি random ইন্টিজার
random_int = random.randint(1, 10)
print(f"Random number (1-10): {random_int}")

# লিস্ট থেকে একটি random আইটেম বাছাই
choices = ['apple', 'banana', 'cherry']
random_choice = random.choice(choices)
print(f"Random fruit: {random_choice}")