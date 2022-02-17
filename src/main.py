from typing import AnyStr
import numpy

# stores messages before encryption and after decryption
decrypted_msgs = []
# stores messages after they are encrypted
encrypted_msgs = []
# stores signatures to be verified
signatures = []


def main():
    while(True):
        print('''
Please select your user type:
    1. A public user
    2. The owner of the keys
    3. Exit program
        ''')

        option = input("\nEnter your choice: ")

        if option == "1":
            public_user_menu()
        elif option == "2":
            key_owner_menu()
        elif option == "3":
            exit()
        else:
            print("please enter '1', '2', or '3'")


def public_user_menu():
    while (True):
        print('''      
As a public user, what would you like to do?
    1. Send an encrypted message
    2. Authenticate a digital signature
    3. Exit
        ''')
        option = input("\nEnter your choice: ")

        # accepts message and stores in decryptedMsgs
        if option == "1":
            decrypted_msgs.append(input("\nEnter a message: "))
            # moves from decrypted to encrypted with basic encryption tester
            encrypted_msgs.append(decrypted_msgs.pop(
                decrypted_msgs.count(str) - 1))

            # TODO add call to run encryption on last decrypted message added
            print("message encrypted and sent.")

        # checks for signatures
        elif option == "2":
            if signatures == []:
                print("There are no signatures to authenticate")
            # show signature options
            else:
                print("The following messages are available:")
                print(
                    [f'\t{encrypted_msgs.index(s)+1} . (length = {len(s)})\n' for s in signatures])

                selected_sig = signatures[int(input("Enter your choice: "))-1]
                print(selected_sig)

            # TODO add call to verify signature

        elif option == "3":
            break
        else:
            print("please enter '1', '2', or '3'")


def key_owner_menu():
    while True:
        # print menu
        print('''
As the owner of the keys, what would you like to do?
    1. decrypt a received message
    2. digitally sign a message
    3. Exit
        ''')

        # get user input
        option = input("\nEnter your choice: ")

        # checks for enctyped messages
        if option == "1":
            if encrypted_msgs == []:
                print("There are no messages available.")
            else:
                print("The following messages are available:")

                # display encrypted Messages by length
                print(
                    [f'\t{encrypted_msgs.index(s)+1} . (length = {len(s)})\n' for s in encrypted_msgs])

                selected_msg = encrypted_msgs[int(
                    input("Enter your choice: "))-1]

                # TODO insert call to decryption method
                print(selected_msg)
        # add signature to signatures list
        elif option == "2":
            signatures.append(input("Enter a message:"))
            print("Message signed and sent.")
        # exit to main
        elif option == "3":
            break
        # catch case
        else:
            print("please enter '1', '2', or '3'")


# once mainMenu is ran stuck in recursive loop between menus
# functions unless option 3 is selected while in the main menu
main()
