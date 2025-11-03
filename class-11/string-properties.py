# Python String Properties - গুরুত্বপূর্ণ স্ট্রিং প্রোপার্টিজ

# ১. স্ট্রিং ইমমিউটেবল (Immutable) - একবার তৈরি হলে পরিবর্তন করা যায় না
text = "Python"
print(f"Original text: {text}")
# text[0] = "J"  # এটি error দেবে কারণ string immutable

# নতুন string তৈরি করতে হয়
new_text = "J" + text[1:]
print(f"New text: {new_text}")

print("\n" + "="*50 + "\n")

# ২. স্ট্রিং লেংথ (Length) - len() ফাংশন দিয়ে দৈর্ঘ্য বের করা
name = "বাংলাদেশ"
print(f"String: {name}")
print(f"Length: {len(name)} টি অক্ষর")

english_text = "Bangladesh"
print(f"\nString: {english_text}")
print(f"Length: {len(english_text)} characters")

print("\n" + "="*50 + "\n")

# ৩. স্ট্রিং ইন্ডেক্সিং (Indexing) - প্রতিটি অক্ষরের একটি পজিশন আছে
word = "Python"
print(f"String: {word}")
print(f"First character (index 0): {word[0]}")
print(f"Last character (index -1): {word[-1]}")
print(f"Third character (index 2): {word[2]}")

print("\n" + "="*50 + "\n")

# ৪. স্ট্রিং স্লাইসিং (Slicing) - একাধিক অক্ষর একসাথে নেওয়া
text = "Bangladesh"
print(f"Full string: {text}")
print(f"First 5 characters [0:5]: {text[0:5]}")
print(f"Last 4 characters [-4:]: {text[-4:]}")
print(f"Middle part [2:6]: {text[2:6]}")
print(f"Every 2nd character [::2]: {text[::2]}")
print(f"Reverse string [::-1]: {text[::-1]}")

print("\n" + "="*50 + "\n")

# ৫. স্ট্রিং কনক্যাটেনেশন (Concatenation) - যোগ করা
first_name = "মোহাম্মদ"
last_name = "রহিম"
full_name = first_name + " " + last_name
print(f"First name: {first_name}")
print(f"Last name: {last_name}")
print(f"Full name: {full_name}")

print("\n" + "="*50 + "\n")

# ৬. স্ট্রিং রিপিটিশন (Repetition) - পুনরাবৃত্তি করা
symbol = "* "
print(f"Symbol: '{symbol}'")
print(f"Repeated 10 times: {symbol * 10}")

line = "-"
print(f"\nDivider line: {line * 50}")

print("\n" + "="*50 + "\n")

# ৭. মেম্বারশিপ অপারেটর (Membership) - in এবং not in
sentence = "আমি বাংলায় গান গাই"
print(f"Sentence: {sentence}")
print(f"'বাংলায়' আছে কি? {('বাংলায়' in sentence)}")
print(f"'ইংরেজি' নেই কি? {('ইংরেজি' not in sentence)}")

email = "user@example.com"
print(f"\nEmail: {email}")
print(f"'@' symbol আছে কি? {('@' in email)}")

print("\n" + "="*50 + "\n")

# ৮. স্ট্রিং কেস সেন্সিটিভ (Case Sensitive) - বড় ছোট হাতের পার্থক্য থাকে
word1 = "Python"
word2 = "python"
word3 = "PYTHON"

print(f"word1: {word1}")
print(f"word2: {word2}")
print(f"word3: {word3}")
print(f"\nword1 == word2? {word1 == word2}")
print(f"word1 == word3? {word1 == word3}")
print(f"word2 == word3? {word2 == word3}")

# Case insensitive comparison - ছোট হাতে কনভার্ট করে তুলনা
print(f"\nCase insensitive: word1.lower() == word2.lower()? {word1.lower() == word2.lower()}")

print("\n" + "="*50 + "\n")

# ৯. স্ট্রিং ইটারেশন (Iteration) - লুপ চালানো যায়
word = "Python"
print(f"String: {word}")
print("Each character:")
for char in word:
    print(f"  {char}")

# বাংলা স্ট্রিং এ লুপ
print(f"\nBangla string: বাংলা")
for char in "বাংলা":
    print(f"  {char}")

print("\n" + "="*50 + "\n")

# ১০. মাল্টি-লাইন স্ট্রিং (Multi-line String) - তিনটি কোট ব্যবহার করে
multi_line = """এটি একটি 
মাল্টি-লাইন 
স্ট্রিং"""

print("Multi-line string:")
print(multi_line)

poem = '''আমার সোনার বাংলা
আমি তোমায় ভালোবাসি
চিরদিন তোমার আকাশ'''

print("\nPoem:")
print(poem)

print("\n" + "="*50 + "\n")

# ১১. এস্কেপ সিকোয়েন্স (Escape Sequences)
print("Escape Sequences:")
print("New line: Hello\\nWorld")
print("Hello\nWorld")

print("\nTab: Name\\tAge")
print("Name\tAge")

print("\nBackslash: C:\\\\Users\\\\Documents")
print("Quote: He said, \\\"Hello\\\"")
print("He said, \"Hello\"")

print("\n" + "="*50 + "\n")

# ১২. Raw String - এস্কেপ সিকোয়েন্স ignore করে
normal_string = "C:\new\test"
raw_string = r"C:\new\test"

print("Normal string:", normal_string)
print("Raw string:", raw_string)

print("\n" + "="*50 + "\n")

# ১৩. স্ট্রিং কম্পারিজন (Comparison) - তুলনা করা যায়
print("String comparison:")
print(f"'apple' < 'banana': {'apple' < 'banana'}")
print(f"'zebra' > 'apple': {'zebra' > 'apple'}")
print(f"'ABC' < 'abc': {'ABC' < 'abc'}  # ASCII value অনুযায়ী")

print("\n" + "="*50 + "\n")

# ১৪. স্ট্রিং ফরম্যাটিং (Formatting) - বিভিন্ন উপায়ে ফরম্যাট করা
name = "রহিম"
age = 25
city = "ঢাকা"

# f-string (recommended)
print(f"আমার নাম {name}, বয়স {age} বছর এবং আমি {city} তে থাকি")

# format() method
print("আমার নাম {}, বয়স {} বছর".format(name, age))

# % formatting (old style)
print("আমার নাম %s, বয়স %d বছর" % (name, age))

print("\n" + "="*50 + "\n")

# ১৫. স্ট্রিং আইডেন্টিটি (Identity) - is এবং is not
str1 = "Python"
str2 = "Python"
str3 = "Py" + "thon"

print(f"str1: {str1}, id: {id(str1)}")
print(f"str2: {str2}, id: {id(str2)}")
print(f"str3: {str3}, id: {id(str3)}")

print(f"\nstr1 is str2: {str1 is str2}  # String interning এর জন্য")
print(f"str1 == str2: {str1 == str2}")
print(f"str1 is str3: {str1 is str3}")
print(f"str1 == str3: {str1 == str3}")

print("\n" + "="*50 + "\n")

print("🎉 Python String Properties সম্পন্ন! 🎉")
