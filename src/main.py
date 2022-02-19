from typing import AnyStr
import backend as b

# stores messages before encryption and after decryption
decrypted_msgs = []
# stores messages after they are encrypted
encrypted_msgs = []
# stores signatures to be verified
signed_msgs = []
n = b.generate_n(b.generate_prime_number(), b.generate_prime_number())
public_key = b.generate_public_key(n)
private_key = b.generate_private_key(public_key[0], n)


def int_input(msg: AnyStr) -> int:
    return int(input(msg))


def main() -> None:
    while(True):
        print(
            'Please select your user type:',
            '\t1. A public user',
            '\t2. The owner of the keys',
            '\t3. Exit program',
            sep='\n')

        option = input("\nEnter your choice: ")

        if option == "1":
            public_user_menu()
        elif option == "2":
            key_owner_menu()
        elif option == "3":
            exit()
        else:
            print("please enter '1', '2', or '3'")


def public_user_menu() -> None:
    while (True):
        print(
            'As a public user, what would you like to do?',
            '\t1. Send an encrypted message',
            '\t2. Authenticate a digital signature',
            '\t3. Exit',
            sep='\n')
        option = input("\nEnter your choice: ")

        if option == "1":
            # accepts message and stores in decrypted_msgs
            encrypted_msgs.append(b.encrypt_message(
                public_key, input("\nEnter a message: ")))

            print("message encrypted and sent.")

        elif option == "2":
            # checks for signatures
            if signed_msgs == []:
                print("There are no signatures to authenticate")
                continue

            # show signature options
            print("The following messages are available:")
            print(*[f'\t{i+1}. (length = {len(s)})'
                    for i, s in enumerate(signed_msgs)], sep="\n")

            selected_sig = signed_msgs[int_input("Enter your choice: ")-1]
            print('signature is valid' if b.authenticate_signature(
                selected_sig[1], public_key, selected_sig[0]) else 'signature is invalid')

        elif option == "3":
            break
        else:
            print("please enter '1', '2', or '3'")


def key_owner_menu() -> None:
    while True:
        print(
            'As the owner of the keys, what would you like to do?',
            '\t1. decrypt a received message',
            '\t2. digitally sign a message',
            '\t3. Exit',
            sep='\n')

        option = input("\nEnter your choice: ")

        if option == "1":
            # checks for enctyped messages
            if encrypted_msgs == []:
                print("There are no messages available.")
                continue

            print("The following messages are available:")
            print(*[f'\t{i+1}. (length = {len(s)})'
                    for i, s in enumerate(encrypted_msgs)], sep="\n")

            selected_msg = encrypted_msgs[int_input("Enter your choice: ")-1]

            print(
                f'Decrypted message: {b.decrypt_message(private_key, selected_msg)}')
        elif option == "2":
            # add signature to signatures list
            signed_msgs.append(b.generate_digital_signature(
                input("Enter a message:"), private_key))
            print("Message signed and sent.")
        elif option == "3":
            break
        else:
            print("please enter '1', '2', or '3'")


main()
