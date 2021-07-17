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

def is_palindrome(s):
    n = len(s)
    i = 0
    while i <= n/2 - 1:
        if (s[i] != s[n-1-i]):
            return False
        i += 1
    return True

ans = []
for i in range(10000, 100000):
    if not is_palindrome(str(i)):
        continue
    if is_prime(i):
        ans.append(i)

print(ans)