# set the password length
PASSWORD_LENGTH = 8

while True:
    # prompt the user for a password
    password = input(f"Enter a password : ")

    # check if the password is of the correct length
    if len(password) == PASSWORD_LENGTH:
        break
    else:
        # if the password is not of the correct length, print asterisks of the same length
        print("*" * len(password))
        print(f"Password wrong.")

# print asterisks of the same length as the password
print("*" * len(password))