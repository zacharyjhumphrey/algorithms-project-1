from typing import AnyStr
from tkinter import N
import random as rnd


def __convert_character_to_number(character: int) -> int:
    return ord(character) #delftStack for ord function information

def __convert_number_to_character(number: int) -> int:
    return chr(number) # geeks for geeks chr function information (test this function. I'm not sure if this will work)

def generate_prime_number() -> int:
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

def generate_n(p: int, q: int) -> tuple:
    return p * q, get_count_coprime_number_count(p, q)

def generate_public_key(n: tuple) -> tuple:
    while (True):
        rand = rnd.randint(2, n[1])
        tested = set()
        if (rand not in tested):
            if (is_coprime(rand, n[1])):
                return rand, n[0]
        tested.add(rand)
    
def generate_private_key(e: int, n: tuple) -> tuple:
    return extended_gcd(e, n[1])[1], n[1]


def encrypt_message(public_key: tuple, message_to_encrypt: AnyStr) -> list[int]:
    # TODO Code review
    # TODO Need to add private key?
    return [
        pow(
            __convert_character_to_number(num), public_key[0]) % public_key[1]
        for num in message_to_encrypt
    ]


def decrypt_message(private_key: tuple, message_to_decrypt: list[int]) -> AnyStr:
    return [  # TODO Code review. dont think this logic is right
        pow(
            __convert_number_to_character(num), private_key[0]) % private_key[1]
        for num in message_to_decrypt
    ]


def generate_digital_signature(msg: AnyStr, private_key: tuple) -> int:
    # TODO type message, but will it be a string or list of numbers
    return pow(msg, private_key[1], private_key[0]) # probably incorrect


def authenticate_signature(msg: AnyStr, public_key: tuple, signature: int) -> AnyStr:
    return pow(signature, public_key[1], public_key[0]) # probably incorrect


def get_count_coprime_number_count(prime_1: int, prime_2: int) -> int:
    return (prime_1 - 1) * (prime_2 - 1)


def is_prime(a: int, n: int) -> bool:
    return pow(a,n-1,n) == 1

def is_coprime(number_to_check_if_coprime: int, N: int) -> bool:
    if (gcd(number_to_check_if_coprime, N) == 1):
        return True
    return False

def gcd(a: int, b: int) -> int:
    if (a < b):
        return gcd(b, a)
    if (a == 0):
        return b
    return gcd(b, a%b)

def extended_gcd(a: int, b: int) -> tuple:
    if (a == 0):
        return b, 0, 1
    
    gcd, x1, y1 = extended_gcd(b%a, a)

    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y
