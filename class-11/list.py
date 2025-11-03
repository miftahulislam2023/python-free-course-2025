fruits = ["apple", "banana", "cherry"]
print(fruits)

# আইটেম যোগ করা
fruits.append("orange") # শেষে যোগ হয়
print(fruits)
fruits.insert(1, "mango") # নির্দিষ্ট ইনডেক্সে যোগ হয়
print(fruits)

# আইটেম সরানো
fruits.remove("banana") # ভ্যালু দিয়ে সরানো
print(fruits)
popped_item = fruits.pop(2) # ইনডেক্স দিয়ে সরানো এবং আইটেমটি রিটার্ন করা
print(fruits)
print(f"সরানো হয়েছে: {popped_item}")
# print(fruits)