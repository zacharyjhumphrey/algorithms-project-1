from backend import *
import random as rnd
import pytest

# def test_convert_character_to_number():
#     pass
#     # assert __convert_character_to_number('a') == 1
#     # assert __convert_character


def test_generate_prime_number():
    # TODO Depends on is potentially prime passing
    for i in range(20):
        prime = generate_prime_number(80, 130)
        for i in range(2, int(prime / 2)):
            if prime % i == 0:
                print(f'generated prime is {prime}')
                pytest.fail(
                    "Test generate prime number has returned a prime number")

# def test_generate_public_key():
#     pass


# def test_generate_private_key(e, phi_N):
#     return 0


# def test_encrypt_message(public_key, message_to_encrypt):
#     pass


# def test_decrypt_message(private_key, message_to_decrypt):
#     pass


# def test_generate_digital_signature(msg, private_key):
#     pass


# def test_authenticate_signature(msg, public_key, private_key):
#     pass


# def test_get_count_coprime_number_count(prime_1, prime_2):
#     pass


# def test_is_coprime(number_to_check_if_coprime, N):
#     pass


def test_gcd():
    for i in range(10):
        x = rnd.randint(2, 70)
        y = x * rnd.randint(2, 70)
        assert gcd(x, y) == x

    for i in range(10):
        x = rnd.randint(2, 70)
        y = 2 * rnd.randint(2, 70)
        z = 3 * rnd.randint(2, 70)
        assert gcd(z, y) == x


def test_gcd_with_prime_numbers():
    for i in range(10):
        x = generate_prime_number(80, 300)
        y = 0
        while y != x:
            y = rnd.randint(80, 300)
        assert gcd(x, y) == 1


# def test_test_failing():
#     assert Example().value < 4
