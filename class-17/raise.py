def withdraw_money(balance, amount):
    if amount < 0:
        # নেগেটিভ টাকা তোলা অসম্ভব, তাই আমরা ValueError রেইজ করলাম
        raise ValueError("টাকার পরিমাণ নেগেটিভ হতে পারে না!")
    
    if amount > balance:
        # ব্যালেন্সের চেয়ে বেশি টাকা চাইলে কাস্টম মেসেজসহ রেইজ
        raise Exception("অ্যাকাউন্টে পর্যাপ্ত ব্যালেন্স নেই!")

    balance -= amount
    print(f"✅ {amount} টাকা তোলা হয়েছে। বর্তমান ব্যালেন্স: {balance}")
    return balance

# কোড টেস্ট করা
current_balance = 5000

try:
    withdraw_money(current_balance, -100) # এটি ValueError তৈরি করবে
except ValueError as e:
    print(f"ইনপুট এরর: {e}")
except Exception as e:
    print(f"ট্রানজেকশন ফেইলড: {e}")

try:
    withdraw_money(current_balance, 6000) # এটি পর্যাপ্ত ব্যালেন্স নেই এরর দিবে
except Exception as e:
    print(f"দুঃখিত: {e}")

# সঠিক ব্যবহার
try:
    withdraw_money(current_balance, 500) # এটি পর্যাপ্ত ব্যালেন্স নেই এরর দিবে
except Exception as e:
    print(f"দুঃখিত: {e}")