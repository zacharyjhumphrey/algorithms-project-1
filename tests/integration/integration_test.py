from backend import *


def test_integrate():
    for i in range(10):
        p = generate_prime_number()
        q = generate_prime_number()
        n = generate_n(p, q)
        public_key = generate_public_key(n)
        private_key = generate_private_key(public_key[0], n)
        print(p, q)

        # TODO random string
        msg = 'B'
        e_msg = encrypt_message(public_key, msg)
        d_msg = decrypt_message(private_key, e_msg)
        print(d_msg)

        assert public_key[0] * private_key[0] % n[1] == 1
