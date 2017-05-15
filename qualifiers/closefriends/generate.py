#!/usr/bin/python

from gmpy2 import *
from Crypto.Util.number import *

Nbits = 1024

flag = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

def is_safe_prime(p):
    return isPrime(p) and isPrime((p - 1) / 2)

def generate_RSA():
    min_p = getRandomNBitInteger(Nbits)
    p = min_p
    while True:
        print (p)
        p = next_prime(p)
        if is_safe_prime(p):
            break
    min_q = p
    q = min_q
    while True:
        print (q)
        q = next_prime(q)
        if is_safe_prime(q):
            break
    assert is_safe_prime(p) and is_safe_prime(q)
    # we have 2 safe prime numbers
    print ("Found p:"+p)
    print (q)
    n = p * q
    phi = (p - 1) * (q - 1)
    # common 
    e = 65537
    d = invert(e, phi)
    return n, e, d

n, e, d = generate_RSA()

m = bytes_to_long(flag)
c = powmod(m, e, n)

assert long_to_bytes(powmod(c, d, n)) == flag

print (n)
print (c)
