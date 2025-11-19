import sys
# --- Sys মডিউল ---
# পাইথনের ভার্সন চেক করা
print(f"Python version: {sys.version.split()[0]}")

# টার্মিনাল থেকে দেওয়া আর্গুমেন্ট (যেমন: python script.py arg1 arg2)
print(f"Command line arguments: {sys.argv}")

# python3 sys.py ja iccha likhbo
# Python version: 3.14.0
# Command line arguments: ['sys.py', 'ja', 'iccha', 'likhbo']