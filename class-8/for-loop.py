# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]
dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020   # duplicate key; last one (2020) will overwrite the previous
}

for key, value in dict.items():
    print(key, value)
