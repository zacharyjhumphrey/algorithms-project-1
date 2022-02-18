from backend import *
import random as rnd
import pytest


def test_convert_character_to_number():
    try:
        test = convert_character_to_number('A')
        if (test != 65):
            raise Exception
        pass
    except Exception:
        pytest.fail("Unexpected Exception ..")


def test_convert_number_to_character():
    try:
        test = convert_number_to_character(65)
        if (test != 'A'):
            raise Exception
        pass
    except Exception:
        pytest.fail("Uncexpected Exception ..")


def test_generate_prime_number():
    # TODO Depends on is potentially prime passing
    for i in range(20):
        prime = generate_prime_number(80, 130)
        for i in range(2, int(prime / 2)):
            if prime % i == 0:
                pytest.fail(
                    "Test generate prime number has returned a prime number")


def test_generate_n():
    try:
        test = generate_n(2, 7)
        if (test[0] != 14):
            raise Exception
        if (test[1] != 6):
            raise Exception
        pass
    except Exception:
        pytest.fail("Unexpected Exception ..")


def test_generate_public_key():
    pass

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


def test_get_count_coprime_number_count():
    try:
        test = get_count_coprime_number_count(2, 7)
        if (test != 6):
            raise Exception
        pass
    except Exception:
        pytest.fail("Unexpected Exception ..")


def test_is_potentially_prime():
    try:
        if (not is_potentially_prime(3, 7)):
            raise Exception
        if (is_potentially_prime(5, 8)):
            raise Exception
        pass
    except Exception:
        pytest.fail("Unexpected Exception ..")


def test_is_coprime():
    assert is_coprime(3, 5)
    assert not is_coprime(3, 9)


# def test_extended_gcd():
#     pass


def test_gcd():
    for i in range(10):
        x = rnd.randint(2, 70)
        y = x * rnd.randint(2, 70)
        assert gcd(x, y) == x

    for i in range(10):
        x = rnd.randint(2, 70)
        y = 2 * x
        z = 3 * x
        assert gcd(z, y) == x


def test_gcd_with_prime_numbers():
    for i in range(10):
        x = generate_prime_number(80, 300)
        y = x
        while y == x:
            y = rnd.randint(80, 300)
        assert gcd(x, y) == 1
