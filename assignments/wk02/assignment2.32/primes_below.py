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

def primes_below(n):
    ans = []
    i = 2
    while i < n:
        if is_prime(i):
            ans.append(i)
        i += 1
    return ans

if __name__ == '__main__':
    print(primes_below(17))
    print(primes_below(8))
    print(primes_below(2))