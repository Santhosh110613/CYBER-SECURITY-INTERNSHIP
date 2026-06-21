import re
import random
import string

used_passwords = [
    "Admin@123",
    "Welcome@123",
    "Password@123"
]

def check_password_strength(password):

    score = 0

    # Length Check
    if len(password) >= 8:
        score += 1

    # Uppercase Check
    if re.search(r"[A-Z]", password):
        score += 1

    # Lowercase Check
    if re.search(r"[a-z]", password):
        score += 1

    # Number Check
    if re.search(r"\d", password):
        score += 1

    # Special Character Check
    if re.search(r"[!@#$%^&*()_+=\-{}[\]:;,.?/]", password):
        score += 1

    return score


def generate_strong_password():

    chars = string.ascii_letters + string.digits + "!@#$%^&*"

    password = "".join(random.choice(chars) for _ in range(12))

    return password


print("=" * 40)
print("PASSWORD STRENGTH ANALYZER")
print("=" * 40)

password = input("Enter Password: ")

print("\nAnalyzing Password...\n")

# Uniqueness Check
if password in used_passwords:
    print("❌ Password already used before!")
else:
    print("✅ Password is unique")

score = check_password_strength(password)

print("\nPassword Analysis")
print("-" * 20)

print("Length :", len(password))

if score <= 2:
    print("Strength : WEAK")
elif score <= 4:
    print("Strength : MEDIUM")
else:
    print("Strength : STRONG")

print("\nSecurity Checks")

print("Uppercase :", bool(re.search(r"[A-Z]", password)))
print("Lowercase :", bool(re.search(r"[a-z]", password)))
print("Numbers   :", bool(re.search(r"\d", password)))
print("Special   :", bool(re.search(r"[!@#$%^&*()_+=\-{}[\]:;,.?/]", password)))

if score < 5:
    print("\nSuggested Strong Password:")
    print(generate_strong_password())

print("\nProgram Completed Successfully")