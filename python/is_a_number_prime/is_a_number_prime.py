from math import isqrt

def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    return all(num % d != 0 for d in range(3, isqrt(num) + 1, 2))

print(is_prime(73))  # True
print(is_prime(75))  # False
print(is_prime(-1))  # False