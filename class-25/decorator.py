# এটি আমাদের ডেকোরেটর ফাংশন
def make_pretty(func):
    def inner():
        print("I got decorated") # অতিরিক্ত কাজ
        func() # মূল ফাংশন কল
    return inner

# ডেকোরেটর ব্যবহার
@make_pretty
def ordinary_function():
    print("I am ordinary function")

ordinary_function()

# আউটপুট:
# I got decorated
# I am ordinary