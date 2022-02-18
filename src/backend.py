from typing import AnyStr
import random as rnd


def convert_character_to_number(character: AnyStr) -> int:
    return ord(character) - ord('A') + 1


def convert_number_to_character(number: int) -> int:
    return chr(number + 64)


def generate_prime_number(lower_bound: int = 100000, upper_bound: int = 1000000) -> int:
    while (True):
        n = rnd.randint(lower_bound, upper_bound)
        if is_prime(n):
            return n


def generate_n(p: int, q: int) -> tuple:
    return p * q, get_count_coprime_number_count(p, q)


def generate_public_key(n: tuple) -> tuple:
    N, phi_N = n
    tested = set()
    while True:
        e = rnd.randint(2, phi_N)
        if e not in tested and is_coprime(e, N) and is_coprime(e, phi_N):
            return e, N
        tested.add(e)


def generate_private_key(e: int, n: tuple) -> tuple:
    # TODO test
    return extended_gcd(e, n[1])[1], n[0]


def encrypt_message(public_key: tuple, message_to_encrypt: AnyStr) -> list[int]:
    """
    encrypt_message _summary_

    Args:
        public_key (tuple): key known by all clients
        message_to_encrypt (AnyStr): _description_

    Returns:
        list[int]: _description_
    """
    # TODO Code review
    # TODO Need to add private key?
    # TODO test
    return [
        pow(
            convert_character_to_number(num), public_key[0], public_key[1])
        for num in message_to_encrypt
    ]


def decrypt_message(private_key: tuple, message_to_decrypt: list[int]) -> AnyStr:
    # TODO Code review. dont think this logic is right
    msg = ""
    for num in message_to_decrypt:
        msg = msg + \
            convert_number_to_character(
                pow(num, private_key[0], private_key[1]))
    return msg
    # return [
    #     convert_number_to_character(
    #         pow(num, private_key[0], private_key[1])
    #     )
    #     for num in message_to_decrypt
    # ]


def generate_digital_signature(msg: AnyStr, private_key: tuple) -> int:
    """
    generate_digital_signature creates a signature for the owner of keys
    This is used to to verify whether or not a message is verified.

    Args:
        msg (AnyStr): message used to create signature
        private_key (tuple): key from the user that created the message

    Returns:
        int: TODO
    """
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
    """
    is_potentially_prime is used to compute whether or not a number is prime.
    This function is correct about 50% of the time. Called multiple times with
    a different a value, this method can nearly assure that a number is prime.

    Args:
        a (int): _description_
        n (int): _description_

    Returns:
        bool: _description_
    """
    return pow(a, n-1, n) == 1


def is_prime(n: int):
    # 99.9% certainty
    # TODO Consider changing it bc low numbers wont work
    return all(is_potentially_prime(a, n) for a in rnd.sample(range(2, n-2), 9))


def is_coprime(number_to_check_if_coprime: int, N: int) -> bool:
    return gcd(number_to_check_if_coprime, N) == 1


def gcd(a: int, b: int) -> int:
    """
    gcd returns the greatest common divisor

    Args:
        a (int): first number
        b (int): second number

    Returns:
        int: great common denominator
    """
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b, a % b)


def extended_gcd(a: int, b: int) -> tuple:
    # TODO test
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x
