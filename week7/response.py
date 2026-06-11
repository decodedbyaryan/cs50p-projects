from validators import email


user_input = email(input("What is your email address? ").lower())

if user_input == True:
    print("Valid")

else:
    print("Invalid")
