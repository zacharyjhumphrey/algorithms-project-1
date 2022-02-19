import functools
from typing import AnyStr, Tuple
import random as rnd


def convert_character_to_number(character: AnyStr) -> int:
    """
    convert_character_to_number turns a character into its number
    value, starting with the space character on the ASCII table

    Args:
        character (AnyStr): character that will be turned into a number

    Returns:
        int: number representation of the character
    """
    return ord(character) - ord(' ') + 1


def convert_number_to_character(number: int) -> AnyStr:
    """
    convert_number_to_character turns a number into the character
    that it is mapped to. The mapping can be seen in the ASCII table
    starting with the space character and moving down the table

    Args:
        number (int): number of the character desired

    Returns:
        AnyStr: character
    """
    return chr(number + ord(' ') - 1)


def generate_prime_number(lower_bound: int = 100000, upper_bound: int = 1000000) -> int:
    """
    generate_prime_number continues finding a random number between given bounds 
    until a prime number is found and returned

    Args:
        lower_bound (int, optional): lower bound of prime generation. Defaults to 100000.
        upper_bound (int, optional): upper bound of prime generation. Defaults to 1000000.

    Returns:
        int: prime number between bounds
    """
    while (True):
        n = rnd.randint(lower_bound, upper_bound)
        if is_prime(n):
            return n


def generate_n(p: int, q: int) -> Tuple[int, int]:
    """
    generate_n computes values necessary for key generation

    Args:
        p (int): prime number
        q (int): prime number

    Returns:
        Tuple[int, int]: (
            product of given values,
            number of coprimes between those values
        )
    """
    return p * q, get_count_coprime_number_count(p, q)


def generate_public_key(n: tuple) -> Tuple[int, int]:
    """
    generate_public_key loops until an encryption (e) value is found
    that is not coprime with either value of n. Until this condition is met,
    values that are not coprime are stored to prevent the unnessary computations

    Args:
        n (tuple): values required to generate key

    Returns:
        Tuple[int, int]: public key
    """
    N, phi_N = n
    tested = set()
    while True:
        e = rnd.randint(2, phi_N)
        if e not in tested and is_coprime(e, N) and is_coprime(e, phi_N):
            return e, N
        tested.add(e)


def generate_private_key(e: int, n: tuple) -> Tuple[int, int]:
    """
    generate_private_key creates a private key using Euclid's extended
    GCD method

    Args:
        e (int): encryption integer
        n (tuple): values required for key generation

    Returns:
        Tuple[int, int]: private key
    """
    return (extended_gcd(e, n[1])[1] % n[1]) + n[1], n[0]


def encrypt_message(public_key: tuple, message_to_encrypt: AnyStr) -> list[int]:
    """
    encrypt_message converts an character into its mapped number value 
    and then encrypts it by raising it to the power of public_key[0]
    modulus public_key[1]

    Args:
        public_key (tuple): key known by all clients
        message_to_encrypt (AnyStr): message to be encrypted

    Returns:
        list[int]: encrypted message
    """
    return [
        pow(
            convert_character_to_number(num), public_key[0], public_key[1])
        for num in message_to_encrypt
    ]


def decrypt_message(private_key: tuple, message_to_decrypt: list[int]) -> AnyStr:
    """
    decrypt_message converts an number into its mapped character value 
    and then encrypts it by raising it to the power of private_key[0]
    modulus private_key[1]

    Args:
        private_key (tuple): private key
        message_to_decrypt (list[int]): message to decrypt

    Returns:
        AnyStr: _description_
    """
    # TODO Code review. dont think this logic is right
    return functools.reduce(
        lambda s, num: s + convert_number_to_character(
            pow(num, private_key[0], private_key[1])),
        message_to_decrypt, '')


def generate_digital_signature(msg: AnyStr, private_key: tuple) -> tuple:
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
    signature = []
    for num in msg:
        signature.append(pow(convert_character_to_number(num),
                         private_key[0], private_key[1]))
    return signature, msg


def authenticate_signature(msg: AnyStr, public_key: tuple, signature: list[int]) -> bool:
    # TODO test
    # probably incorrect
    test = ""
    for num in signature:
        test = test + \
            convert_number_to_character(pow(num, public_key[0], public_key[1]))
    return test == msg


def get_count_coprime_number_count(prime_1: int, prime_2: int) -> int:
    """
    get_count_coprime_number_count returns the number of coprime numbers
    between prime_1 and prime_2

    Args:
        prime_1 (int): prime number
        prime_2 (int): prime number

    Returns:
        int: number of coprimes in the given range
    """
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


def is_prime(n: int) -> bool:
    """
    is_prime determines (with 99.8% certainty) if a number is prime. 
    To do this, the function passes the given number and a random number 
    into is_potentially_prime (a function that determines if the given number 
    meets a condition). If it does meet that condition, the test is ran with 
    more random numbers to make sure this is a prime number

    Args:
        n (int): number to check if prime

    Returns:
        bool: whether or not a number is prime
    """
    # 99.9% certainty
    # TODO Consider changing it bc low numbers wont work
    return all(is_potentially_prime(a, n) for a in rnd.sample(range(2, n-2), 9))


def is_coprime(a: int, b: int) -> bool:
    """
    is_coprime determines the greatest common factor of 
    two numbers, and if this number is 1, the
    numbers are said to be coprime (they share no common factors 
    other than 1)

    Args:
        a (int): some number 
        b (int): some number

    Returns:
        bool: whether or not the numbers are coprime
    """
    return gcd(a, b) == 1


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


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    extended_gcd TODO docme

    Args:
        a (int): _description_
        b (int): _description_

    Returns:
        Tuple[int, int, int]: _description_
    """
    # TODO test
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x
