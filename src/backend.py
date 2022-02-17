
from tkinter import N
import random as rnd


def convert_character_to_number(character):
    return ord(character) #delftStack for ord function information

def convert_number_to_character(number):
    return chr(number) #geeks for geeks chr function information (test this function. I'm not sure if this will work)

def generate_prime_number():
    while (True):
        n = rnd.randint(100000, 1000000)
        tested = set()
        while (len(tested) < 9):
            a = rnd.randint(2, n - 2)
            if (a not in tested):
                if (is_prime(a, n)):
                    tested.add(a)
                else:
                    continue
            if (len(tested) == 8):
                return n

def generate_public_key(p, q):
    return 0

def generate_private_key(e, phi_N):
    return 0

def encrypt_message(public_key, message_to_encrypt):
    encrypted = []

    for i in range(len(message_to_encrypt)):
       encrypted[i] = pow(convert_character_to_number(message_to_encrypt[i]), public_key[0], public_key[1])
    
    return encrypted

def decrypt_message(private_key, message_to_decrypt):
    encrypted = []

    for i in range(len(message_to_decrypt)):
        encrypted[i] = convert_number_to_character(pow(message_to_decrypt[i], private_key[0], private_key[1]))

    return encrypted

def generate_digital_signature(msg, private_key):
    return 0

def authenticate_signature(msg, public_key, private_key):
    return 0

def get_count_coprime_number_count(prime_1, prime_2):
    return (prime_1 - 1) * (prime_2 - 1)

def is_coprime(number_to_check_if_coprime, N):
    return True

def is_prime(a, n):
    return pow(a,n-1,n) == 1