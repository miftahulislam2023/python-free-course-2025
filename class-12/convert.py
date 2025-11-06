# লিস্ট থেকে টাপলে
my_list = ["a", "b", "c"]
my_tuple = tuple(my_list)
print(f"লিস্ট থেকে টাপল: {my_tuple}")

# টাপল থেকে সেটে (ডুপ্লিকেট বাদ যাবে)
my_tuple_with_duplicates = (1, 2, 2, 3, 4, 3)
my_set = set(my_tuple_with_duplicates)
print(f"টাপল থেকে সেট: {my_set}") 

# সেট থেকে লিস্টে
my_list_from_set = list(my_set)
print(f"সেট থেকে লিস্ট: {my_list_from_set}") 

# টাপলের লিস্ট থেকে ডিকশনারিতে
list_of_tuples = [("name", "Rahim"), ("age", 25)]
my_dict = dict(list_of_tuples)
print(f"টাপল লিস্ট থেকে ডিকশনারি: {my_dict}")