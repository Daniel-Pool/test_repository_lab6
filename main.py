#Daniel Pool's Repository "test_repository_lab6"

def encoder (code):
    encoded = ""
    for i in code:
        encoded += str((int(i) + 3) % 10)
    return encoded


def decode(code): #Steven Lin's Part
    pass


def selected_option(user_option):
    global encoded_password
    global decoded_password
    global original_password
    global cont

    if user_option == '1':
        original_password = input("Please enter your password to encode: ")
        encoded_password = encoder(original_password)
        print("Your password has been encoded and stored!")

    if user_option == '2':
        decoded_password = decode(encoded_password)
        print(f"The encoded password is {encoded_password}, and the original password is {original_password}")

    if user_option == '3':
        cont = False


def main():
    global encoded_password
    global decoded_password
    global original_password
    global cont

    cont = True
    while cont:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print("")

        options = input("Please enter an option: ")
        selected_option(options)


if __name__ == '__main__':
    encoded_password = ""
    decoded_password = ""
    original_password = ""
    main()