# -------------------------------
# Password Strength Checker
# Developed in Python
# -------------------------------

password = input("Enter your password: ")

# Check if password is empty
if not password:
    print("Error: Password cannot be empty.")
    exit()

has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
symbols = "!@#$%^&*()-_=+[]{}|;:',.<>/?"
has_symbol = any(char in symbols for char in password)

common_passwords = [
    "password", "123456", "12345678", "qwerty", "abc123", 
    "password123", "admin", "welcome", "letmein", "111111"
]

score = 0

if len(password) >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_symbol:
    score += 1

print("\n----------- Password Analysis -----------")
print("Length:", len(password))
print("Uppercase:", has_upper)
print("Lowercase:", has_lower)
print("Numbers:", has_digit)
print("Symbols:", has_symbol)

if password.lower() in common_passwords:
    print("\n❌ This is a commonly used password.")
    print("Password Strength: VERY WEAK")
    print("Choose a unique password.")
else:
    print("\nScore:", score, "/5")

    if score == 5:
        print("✅ Password Strength: STRONG")
    elif score >= 3:
        print("🟡 Password Strength: MEDIUM")
    else:
        print("🔴 Password Strength: WEAK")
    
    print("\nSuggestions to Improve Password:")
    if len(password) < 8:
        print("- Use at least 8 characters.")
    if not has_upper:
        print("- Add at least one uppercase letter (A-Z).")
    if not has_lower:
        print("- Add at least one lowercase letter (a-z).")
    if not has_digit:
        print("- Add at least one number (0-9).")
    if not has_symbol:
        print("- Add at least one special symbol (!,@,#,$,etc).")

    if score == 5 and password.lower() not in common_passwords:
        print("\nExcellent! Your password follows all recommended security practices.")