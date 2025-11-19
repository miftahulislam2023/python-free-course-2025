import os

# --- OS মডিউল ---
# বর্তমান ডিরেক্টরি (যেখানে ফাইলটি রান হচ্ছে)
current_dir = os.getcwd()
print(f"Current Directory: {current_dir}")

# ডিরেক্টরিতে কী কী ফাইল বা ফোল্ডার আছে
dir_list = os.listdir('.') # '.' মানে বর্তমান ডিরেক্টরি
print(f"Files in current dir: {dir_list}")