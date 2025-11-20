# import os
# # বর্তমান ডিরেক্টরি বা ফোল্ডার জানা
# current_dir = os.getcwd()
# print(f"বর্তমান লোকেশন: {current_dir}")

# # ক্রস-প্ল্যাটফর্ম পাথ তৈরি
# folder_name = "class-15"
# file_name = "notes.txt"

# # os.path.join অটোমেটিক স্ল্যাশ ( / অথবা \ ) ঠিক করে নেয়
# full_path = os.path.join(current_dir, folder_name, file_name)

# print(f"তৈরিকৃত পাথ: {full_path}")
# # Windows এ আউটপুট হবে: ...\documents\notes.txt
# # Linux/Mac এ আউটপুট হবে: .../documents/notes.txt

from pathlib import Path

# ফোল্ডার এবং ফাইলের নাম সেট করা
base_path = Path("class-15")
full_path = base_path / "notes.txt"  # স্ল্যাশ (/) অপারেটর দিয়েই পাথ জোড়া লাগানো যায়!

print(f"Pathlib পাথ: {full_path}")


with open(full_path, 'w') as f:
    f.write('This is a note from Miftahul Islam. Academic head of Neural Gem.')