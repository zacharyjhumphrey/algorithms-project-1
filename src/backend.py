from typing import AnyStr
import random as rnd


def convert_character_to_number(character: int) -> int:
    return ord(character)


def convert_number_to_character(number: int) -> int:
    return chr(number)


def generate_prime_number(lower_bound: int = 100000, upper_bound: int = 1000000) -> int:
    while (True):
        n = rnd.randint(lower_bound, upper_bound)
        if is_prime(n):
            return n


def generate_n(p: int, q: int) -> tuple:
    return p * q, get_count_coprime_number_count(p, q)


def generate_public_key(n: tuple) -> tuple:
    # TODO test
    while (True):
        rand = rnd.randint(2, n[1])
        tested = set()
        if rand not in tested and is_coprime(rand, n[1]):
            return rand, n[0]
        tested.add(rand)


def generate_private_key(e: int, n: tuple) -> tuple:
    # TODO test
    return extended_gcd(e, n[1])[1], n[1]


def encrypt_message(public_key: tuple, message_to_encrypt: AnyStr) -> list[int]:
    # TODO Code review
    # TODO Need to add private key?
    # TODO test
    return [
        pow(
            convert_character_to_number(num), public_key[0]) % public_key[1]
        for num in message_to_encrypt
    ]


def decrypt_message(private_key: tuple, message_to_decrypt: list[int]) -> AnyStr:
    # TODO Code review. dont think this logic is right
    return [
        pow(
            convert_number_to_character(num), private_key[0]) % private_key[1]
        for num in message_to_decrypt
    ]


def generate_digital_signature(msg: AnyStr, private_key: tuple) -> int:
    # TODO type message, but will it be a string or list of numbers
    # TODO test
    return pow(msg, private_key[1], private_key[0])  # probably incorrect


def authenticate_signature(msg: AnyStr, public_key: tuple, signature: int) -> bool:
    # TODO test
    # probably incorrect
    return pow(signature, public_key[1], public_key[0]) == msg


def get_count_coprime_number_count(prime_1: int, prime_2: int) -> int:
    return (prime_1 - 1) * (prime_2 - 1)


def is_potentially_prime(a: int, n: int) -> bool:
    return pow(a, n-1, n) == 1


def is_prime(n: int):
    # 99.9% certainty
    # TODO Consider changing it bc low numbers wont work
    return all(is_potentially_prime(a, n) for a in rnd.sample(range(2, n-2), 9))


def is_coprime(number_to_check_if_coprime: int, N: int) -> bool:
    return gcd(number_to_check_if_coprime, N) == 1


def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b, a % b)


def extended_gcd(a: int, b: int) -> tuple:
    # TODO test
    if (a == 0):
        return b, 0, 1

    gcd, x1, y1 = extended_gcd(b % a, a)

    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y
