# একটি গ্লোবাল লিস্ট যেখানে সব স্টুডেন্ট ডিকশনারি হিসেবে থাকবে
students = []

def add_student():
    """নতুন শিক্ষার্থী রেকর্ড যোগ করে।"""
    name = input("শিক্ষার্থীর নাম: ")
    roll = input("রোল নম্বর: ")
    
    # ইনপুট ভ্যালিডেশন
    if not name or not roll.isdigit():
        print("ত্রুটি: নাম ও রোল সঠিকভাবে দিন।")
        return

    # প্রতিটি শিক্ষার্থী একটি ডিকশনারি
    student_record = {
        "name": name,
        "roll": int(roll)
    }
    students.append(student_record)
    print(f"রেকর্ড সফলভাবে যোগ হয়েছে: {name}, রোল: {roll}")

def view_all_students():
    """সংরক্ষিত সকল শিক্ষার্থীর রেকর্ড দেখায়।"""
    if not students:
        print("কোনো রেকর্ড পাওয়া যায়নি।")
        return

    print("\n--- সকল শিক্ষার্থীর রেকর্ড ---")
    for student in students:
        print(f"নাম: {student['name']} | রোল: {student['roll']}")
    print("------------------------------\n")

def main_menu():
    """মূল মেনু প্রদর্শন করে এবং ইউজারের ইনপুট অনুযায়ী ফাংশন কল করে।"""
    while True:
        print("\n--- স্টুডেন্ট রেকর্ড ম্যানেজার ---")
        print("1. নতুন শিক্ষার্থী যোগ করুন")
        print("2. সকল রেকর্ড দেখুন")
        print("3. প্রোগ্রাম বন্ধ করুন")
        
        choice = input("আপনার পছন্দ লিখুন (1-3): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_all_students()
        elif choice == '3':
            print("প্রোগ্রাম বন্ধ করা হচ্ছে। ধন্যবাদ।")
            break
        else:
            print("ভুল ইনপুট। দয়া করে 1, 2, বা 3 দিন।")

# প্রোগ্রাম শুরু করার জন্য main_menu ফাংশনটি কল করতে হয়:
main_menu()
