# সেট অপারেশনস
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.union(b))         # {1, 2, 3, 4, 5, 6}
print(a.intersection(b))  # {3, 4}
print(a.difference(b))    # {1, 2}
print(b.difference(a))    # {5, 6}
