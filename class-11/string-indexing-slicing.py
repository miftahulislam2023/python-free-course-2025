# ইনডেক্সিং ও স্লাইসিং (Indexing & Slicing):
my_string = "Hello, Python!"

# ইনডেক্সিং (একটি অক্ষর বের করা)
print(my_string[0])   # আউটপুট: H (প্রথম অক্ষর)
print(my_string[-1])  # আউটপুট: ! (শেষ অক্ষর)

# স্লাইসিং (একটি অংশ বের করা)
print(my_string[7:13]) # আউটপুট: Python
print(my_string[:5])   # আউটপুট: Hello (শুরু থেকে)
print(my_string[7:])   # আউটপুট: Python! (শেষ পর্যন্ত)
print(my_string[::2])  # আউটপুট: Hlo yhn (এক অক্ষর পর পর)
