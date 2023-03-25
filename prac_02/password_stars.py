def main():

    PASSWORD_LENGTH = 8

    while True:

        password = get_password()


        if len(password) == PASSWORD_LENGTH:
            break
        else:

            the_password(password)
            print(f"Password wrong.")

    the_password(password)


def the_password(password):
    print("*" * len(password))


def get_password():
    password = input(f"Enter a password: ")
    return password


if __name__ == '__main__':
    main()
