#simple password checker

#user input
password = input("Enter your password: ")

#checking length
if len(password) >=8:
    print("Password length is good.")
else:
    print("Password must be at least 8 characters.")

#checking uppercase letters
if any(c.isupper() for c in password):
    print("Contains uppercase letters.")
else :
    print("Add at least one uppercase letter.")

#checking lowercase letter
if any(c.islower() for c in password):
    print("Contains lowercase letters.")
else:
    print("Add at least one lowercase letter.")

#checking digits
if any(c.isdigit() for c in password):
    print("Contains numbers.")
else:
    print("Add at least one number")

#checking special characters
special_characters = "!@#$%^&*(),.?\/:{}|<>;'"
if any(c in special_characters for c in password):
    print("Contains special characters.")
else:
    print("Add at least one special character.")
