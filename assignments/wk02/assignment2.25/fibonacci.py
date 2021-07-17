def big_fibonacci(n):
    if n < 0:
        return None
    num1 = 1
    num2 = 1
    while len(str(num1)) < n:
        keep = num1
        num1 += num2
        num2 = keep
    return num1

if __name__ == '__main__':
    print(big_fibonacci(1))
    print(big_fibonacci(2))
    print(big_fibonacci(3))
    print(big_fibonacci(5))
    print(big_fibonacci(30))