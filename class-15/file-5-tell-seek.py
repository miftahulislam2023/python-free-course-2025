with open("sample.txt", "r", encoding="utf-8") as f:
    # ১০টি ক্যারেক্টার পড়া
    chunk = f.read(10) 
    print(chunk)
    # কার্সর কোথায় আছে দেখা
    print(f.tell())
    chunk = f.read(20) 
    print(chunk)
    print(f.tell())

    # কার্সর আবার শুরুতে নিয়ে যাওয়া
    f.seek(0)
    print(f.tell())