# Password Cracker Program - Using FOR LOOPS
# This program demonstrates how loops work by trying different password combinations

import string

# The password we want to crack
target_password = "1b2d"

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
for length in range(1, 5):
    print(f"\nTrying passwords of length {length}...")
    
    if length == 1:
        # Try all single characters
        for c1 in characters:
            attempts += 1
            guess = c1
            
            # Show progress every 1000 attempts
            if attempts % 1000 == 0:
                print(f"Attempt {attempts}: Trying '{guess}'...")
            
            # Check if we found the password
            if guess == target_password:
                print(f"\n🎉 PASSWORD CRACKED! 🎉")
                print(f"Password: '{guess}'")
                print(f"Total attempts: {attempts}")
                found = True
                break
        
        if found:
            break
    
    elif length == 2:
        # Try all 2-character combinations
        for c1 in characters:
            for c2 in characters:
                attempts += 1
                guess = c1 + c2
                
                if attempts % 1000 == 0:
                    print(f"Attempt {attempts}: Trying '{guess}'...")
                
                if guess == target_password:
                    print(f"\n🎉 PASSWORD CRACKED! 🎉")
                    print(f"Password: '{guess}'")
                    print(f"Total attempts: {attempts}")
                    found = True
                    break
            
            if found:
                break
        
        if found:
            break
    
    elif length == 3:
        # Try all 3-character combinations
        for c1 in characters:
            for c2 in characters:
                for c3 in characters:
                    attempts += 1
                    guess = c1 + c2 + c3
                    
                    if attempts % 1000 == 0:
                        print(f"Attempt {attempts}: Trying '{guess}'...")
                    
                    if guess == target_password:
                        print(f"\n🎉 PASSWORD CRACKED! 🎉")
                        print(f"Password: '{guess}'")
                        print(f"Total attempts: {attempts}")
                        found = True
                        break
                
                if found:
                    break
            
            if found:
                break
        
        if found:
            break
    
    elif length == 4:
        # Try all 4-character combinations
        for c1 in characters:
            for c2 in characters:
                for c3 in characters:
                    for c4 in characters:
                        attempts += 1
                        guess = c1 + c2 + c3 + c4
                        
                        if attempts % 1000 == 0:
                            print(f"Attempt {attempts}: Trying '{guess}'...")
                        
                        if guess == target_password:
                            print(f"\n🎉 PASSWORD CRACKED! 🎉")
                            print(f"Password: '{guess}'")
                            print(f"Total attempts: {attempts}")
                            found = True
                            break
                    
                    if found:
                        break
                
                if found:
                    break
            
            if found:
                break
        
        if found:
            break

if not found:
    print(f"\n❌ Password not found after {attempts} attempts")

print("\n" + "=" * 50)
print("This demonstrates how loops can be used to try multiple combinations!")
