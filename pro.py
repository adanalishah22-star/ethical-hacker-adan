import random
import string
def generate_secure_password():
    print("=== SECURE PASSWORD GENERATOR ===")
    length = 12
    print("password length", length)
    all_characters = "abc123!@#"
    password = ""
    counter = 0
    while counter < length:
        password = password + random.choice(all_characters)
        counter = counter + 1
    print("Generated:", password)
generate_secure_password()
