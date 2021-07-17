def to_hex(n):
    if n < 0 or n > 256:
        return None
    ans = ''
    while True:
        if n < 10:
            ans = ans + str(n)
            return ans[::-1]
        if n < 16:
            ans = ans + chr(87+n)
            return ans[::-1]
        else:
            if n%16 < 10:
                ans = ans + str(n%16)
            elif n%16 < 16:
                ans = ans + chr(87+n%16)
            n = n//16

"""
if __name__ == "__main__":
    print(to_hex(255))
    print(to_hex(25))
    print(to_hex(153))
    print(to_hex(0))
    print(to_hex(-1))
"""