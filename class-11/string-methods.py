# স্ট্রিং মেথডস (কিছু জরুরি মেথড):
text = "  I Love Python Programming!  "
# Case পরিবর্তন
print(text.upper()) # সব বড় হাতের
print(text.lower()) # সব ছোট হাতের
print(text.title()) # প্রতিটি শব্দের প্রথম অক্ষর বড় হাতের

# হোয়াইটস্পেস সরানো
print(text.strip()) # দুই পাশের স্পেস সরানো
print(text.lstrip())# বাম পাশের স্পেস সরানো -> leading whitespace remove করে
print(text.rstrip())# ডান পাশের স্পেস সরানো -> trailing whitespace remove করে

# খোঁজা এবং প্রতিস্থাপন - find and replace
print(text.strip().startswith("I Love")) # True
print(text.count("o")) # 2
print(text.replace("Python", "C"))

name = 'Niftahul Islam'
print(name.startswith('M'))