# Password Cracker Program - Using WHILE LOOPS
# This program demonstrates how while loops work by trying different password combinations

import string

# The password we want to crack
target_password = "abcd"

# Create a list of all possible characters (a-z, A-Z, 0-9)
characters = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
print(f"Character set: {len(characters)} characters")
print(f"Characters: {''.join(characters)}\n")

# Counter to track attempts
attempts = 0
found = False

print(f"Trying to crack password: '{target_password}'")
print("=" * 50)

# Try passwords of different lengths (1 to 4 characters)
length = 1
while length <= 4 and not found:
    print(f"\nTrying passwords of length {length}...")
    
    if length == 1:
        # Try all single characters
        i1 = 0
        while i1 < len(characters) and not found:
            attempts += 1
            guess = characters[i1]
            
            # Show progress every 1000 attempts
            if attempts % 1000 == 0:
                print(f"Attempt {attempts}: Trying '{guess}'...")
            
            # Check if we found the password
            if guess == target_password:
                print(f"\n🎉 PASSWORD CRACKED! 🎉")
                print(f"Password: '{guess}'")
                print(f"Total attempts: {attempts}")
                found = True
            
            i1 += 1
    
    elif length == 2:
        # Try all 2-character combinations
        i1 = 0
        while i1 < len(characters) and not found:
            i2 = 0
            while i2 < len(characters) and not found:
                attempts += 1
                guess = characters[i1] + characters[i2]
                
                if attempts % 1000 == 0:
                    print(f"Attempt {attempts}: Trying '{guess}'...")
                
                if guess == target_password:
                    print(f"\n🎉 PASSWORD CRACKED! 🎉")
                    print(f"Password: '{guess}'")
                    print(f"Total attempts: {attempts}")
                    found = True
                
                i2 += 1
            i1 += 1
    
    elif length == 3:
        # Try all 3-character combinations
        i1 = 0
        while i1 < len(characters) and not found:
            i2 = 0
            while i2 < len(characters) and not found:
                i3 = 0
                while i3 < len(characters) and not found:
                    attempts += 1
                    guess = characters[i1] + characters[i2] + characters[i3]
                    
                    if attempts % 1000 == 0:
                        print(f"Attempt {attempts}: Trying '{guess}'...")
                    
                    if guess == target_password:
                        print(f"\n🎉 PASSWORD CRACKED! 🎉")
                        print(f"Password: '{guess}'")
                        print(f"Total attempts: {attempts}")
                        found = True
                    
                    i3 += 1
                i2 += 1
            i1 += 1
    
    elif length == 4:
        # Try all 4-character combinations
        i1 = 0
        while i1 < len(characters) and not found:
            i2 = 0
            while i2 < len(characters) and not found:
                i3 = 0
                while i3 < len(characters) and not found:
                    i4 = 0
                    while i4 < len(characters) and not found:
                        attempts += 1
                        guess = characters[i1] + characters[i2] + characters[i3] + characters[i4]
                        
                        if attempts % 1000 == 0:
                            print(f"Attempt {attempts}: Trying '{guess}'...")
                        
                        if guess == target_password:
                            print(f"\n🎉 PASSWORD CRACKED! 🎉")
                            print(f"Password: '{guess}'")
                            print(f"Total attempts: {attempts}")
                            found = True
                        
                        i4 += 1
                    i3 += 1
                i2 += 1
            i1 += 1
    
    length += 1

if not found:
    print(f"\n❌ Password not found after {attempts} attempts")

print("\n" + "=" * 50)
print("This demonstrates how while loops can be used to try multiple combinations!")
