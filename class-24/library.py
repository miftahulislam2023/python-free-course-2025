# Features:
# লাইব্রেরিতে বই অ্যাড করা যাবে।
# বই ধার নেওয়া যাবে (যদি এভেইলেবল থাকে)।
# বই ফেরত দেওয়া যাবে।

class Library:
    def __init__(self, name, book_list):
        self.name = name
        self.book_list = book_list
        self.lent_books = {} # কে কোন বই নিয়েছে তার রেকর্ড (Dictionary)

    def display_books(self):
        print(f"\n--- {self.name} এর বইসমূহ ---")
        for book in self.book_list:
            print(f"- {book}")

    def lend_book(self, userName, book):
        if book not in self.book_list:
            print("দুঃখিত, এই বইটি আমাদের লাইব্রেরিতে নেই।")
        elif book in self.lent_books:
            print(f"বইটি বর্তমানে {self.lent_books[book]} এর কাছে আছে। বইটিন ফেরত দিলে আপনি ধার নিতে পারবেন।")
        else:
            self.lent_books[book] = userName
            print(f"অভিনন্দন! '{book}' বইটি আপনার নামে ইস্যু করা হয়েছে।")

    def return_book(self, book):
        if book in self.lent_books:
            del self.lent_books[book]
            print(f"'{book}' বইটি সফলভাবে ফেরত নেওয়া হয়েছে।")
        else:
            print("দুঃখিত, এই বইটি আমাদের এখান থেকে নেওয়া হয়নি।")

# প্রোগ্রাম রান করা
my_library = Library("Neural Gem Library", ["Python Core", "Data Science", "Algorithm"])

while True:
    print("\n1. বই দেখুন\n2. বই ধার নিন\n3. বই ফেরত দিন\n4. বের হন")
    choice = input("অপশন সিলেক্ট করুন: ")

    if choice == "1":
        my_library.display_books()
    elif choice == "2":
        name = input("আপনার নাম: ")
        book = input("বইয়ের নাম: ")
        my_library.lend_book(name, book)
    elif choice == "3":
        book = input("বইয়ের নাম: ")
        my_library.return_book(book)
    elif choice == "4":
        print('Thank you for choosing our library.')
        break
    else:
        print("ভুল অপশন! পুনরায় চেষ্টা করুন")
