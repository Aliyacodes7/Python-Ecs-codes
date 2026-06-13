import re

def validate_phone(phone):
    # Standard phone format: 10 digits, may include h
    pattern = r"^[6-9]\d{9}$"
    return re.fullmatch(pattern, phone) is not None

def validate_email(email):
    # Standard email format
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.fullmatch(pattern, email) is not None

# Get user input
phone = input("Enter your phone number: ")
email = input("Enter your email id: ")

# Validate and display results
if validate_phone(phone):
    print(f"Phone number '{phone}' is valid")
else:
    print(f"Phone number '{phone}' is invalid")

if validate_email(email):
    print(f"Email '{email}' is valid")
else:
    print(f"Email '{email}' is invalid")

input()

'''
sample output
Enter your phone number: 9876543210
Enter your email id: xyz123@gmail.com
Phone number '9876543210' is valid
Email 'xyz123@gmail.com' is valid
'''
