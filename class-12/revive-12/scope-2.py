# ফাংশনের ভিতরে কোন variable থাকলে declare করা হলে তা বাইরে এক্সেস করা যায় না
def square():
    x = 4
    print(x**2)
square()
# print(x)