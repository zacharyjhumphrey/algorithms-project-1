from backend import *
import random as rnd
import pytest


def test_convert_character_to_number():
    test = convert_character_to_number(' ')
    assert(test == 1)


def test_convert_number_to_character():
    test = convert_number_to_character(1)
    assert(test == " ")


def test_generate_prime_number():
    # TODO Depends on is potentially prime passing
    for i in range(20):
        prime = generate_prime_number(80, 130)
        for i in range(2, int(prime / 2)):
            assert prime % i != 0


def test_private_key():
    for i in range(10):
        p = generate_prime_number()
        q = generate_prime_number()
        n = generate_n(p, q)
        public_key = generate_public_key(n)
        private_key = generate_private_key(public_key[0], n)
        print(p, q)

        msg = 'B'
        e_msg = encrypt_message(public_key, msg)
        d_msg = decrypt_message(private_key, e_msg)
        print(d_msg)

        # assert public_key[0] * private_key[0] % n[1] == 1


def test_generate_n():
    assert generate_n(2, 7) == (14, 6)


def test_generate_public_key():
    n = generate_n(2, 7)
    key = generate_public_key(n)
    assert key == (5, 14)


# def test_generate_private_key(e, phi_N):
#     return 0

def test_encrypt_message():
    test = encrypt_message((5, 95), "A")
    assert (test[0] == 59)

def test_decrypt_message():
    test = decrypt_message((11, 95), [59])
    assert test == "A"
    test = decrypt_message((5, 95), [39])
    assert test == "F"

def test_generate_digital_signature():
    test = generate_digital_signature("A", (11, 95))
    assert(test[0][0] == 79)
    assert(test[1] == 'A')

def test_authenticate_signature():
    test = authenticate_signature("A", (5, 95), [79])
    assert(test)


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
    for i in range(1000):
        x = generate_prime_number(150, 300)
        y = x
        while y == x:
            y = rnd.randint(80, 150)
        assert gcd(x, y) == 1
