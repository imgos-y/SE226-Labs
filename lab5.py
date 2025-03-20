import random
import string

change = {}
for _ in range(5):
    char = input("Enter lowercase character: ")
    change[char] = set()
    for _ in range(3):
        change_char = input(f"Enter a replacement for '{char}': ")
        change[char].add(change_char)

# Example password list
passwords = ["fjnvjfkdn", "fhbvdhf", "rdjnskfk"]
print("...Generated new password...")
print(passwords)

# Şifreleri değiştirme
changed_passwords = []
for password in passwords:
    new_password = ""
    changes = 0
    for char in password:
        if char in change:
            new_char = random.choice(list(change[char]))
            new_password += new_char
            changes += 1
        else:
            new_password += char
    changed_passwords.append((new_password, changes))

# Şifreleri kategorize et
categorize_passwords = {"strong": [], "weak": []}
for password, changes in changed_passwords:
    if changes > 4:
        categorize_passwords["strong"].append(password)
    else:
        categorize_passwords["weak"].append(password)

# Sonuçları yazdır
print("\nSTRONG PASSWORDS: ")
for password in categorize_passwords["strong"]:
    print(password)

print("\nWEAK PASSWORDS: ")
for password in categorize_passwords["weak"]:
    print(password)
