import math

def solve_quadratic(a,b,c):
    rt = b**2 - 4*a*c
    if rt == 0:
        return -b/(2*a)
    elif rt > 0:
        return ((-b+math.sqrt(rt))/(2*a), (-b-math.sqrt(rt))/(2*a))
    else:
        return None

"""
if __name__ == "__main__":
    print(solve_quadratic(1,0,0))
    print(solve_quadratic(1,0,1))
    print(solve_quadratic(1,5,6))
"""