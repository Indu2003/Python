def CheckPassword(password):
    if len(password) < 4:
        return False

    has_digit = any(char.isdigit() for char in password)
    has_uppercase = any(char.isupper() for char in password)
    has_special = any(not char.isalnum() for char in password)  # Checks for any non-alphanumeric characters
    is_valid_start = password[0].isalpha()

    return has_digit and has_uppercase and has_special and is_valid_start


password = input("Enter the password: ")
if CheckPassword(password):
    print("The password is strong.")
else:
    print("The password is not strong. Please ensure it meets the following criteria:")
    print("- At least 4 characters long")
    print("- At least one numeric digit")
    print("- At least one uppercase letter")
    print("- Must have at least one non-alphanumeric character")
    print("- Starting character must be a letter")
