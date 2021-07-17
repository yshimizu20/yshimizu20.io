def my_reverse(lst):
    n = len(lst)
    i = 0
    while i <= n/2 - 1:
        keep = lst[i]
        lst[i] = lst[-i-1]
        lst[-i-1] = keep
        i += 1
    return lst

"""
if __name__ == '__main__':
    print(my_reverse([1,2,3,4,5]))
    print(my_reverse([1,2,3,4]))
"""