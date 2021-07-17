def is_prime(n):
    if n < 2:
        return False
    if n in [2,3]:
        return True
    i = 2
    while i**2 <= n:
        if n%i == 0:
            return False
        i += 1
    return True

"""
if __name__ == '__main__':
    print(is_prime(17))
    print(is_prime(5))
    print(is_prime(256))
"""