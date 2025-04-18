def is_square_variant0(n):
    if n < 0:
        return False 
    x = int(n ** 0.5)
    return x * x == n

print(is_square_variant0(25))

def is_square_variant1(n):
    return n >= 0 and (n ** 0.5) % 1 == 0

print(is_square_variant1(25))

import math

def is_square_variant2(n):
    if n < 0:
        return False
    squt = math.sqrt(n)

    return squt.is_integer()

print(is_square_variant2(25))

def is_square_variant3(n):
    return n >= 0 and math.sqrt(n) % 1 == 0
print(is_square_variant3(25))