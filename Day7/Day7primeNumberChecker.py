import math

def prime_checker(n:int):
    is_prime = True
    limit = math.isqrt(n)
    for number in range (2, limit+1):
        if n % number == 0:
            is_prime = False
    if is_prime:
        print("This is a PRIME number!")
    else:
        print("This is NOT aa PRIME number!")

n = int(input("Check this number:"))
prime_checker(n)