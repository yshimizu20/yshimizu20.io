class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def is_valid(self):
        if self.a + self.b < self.c:
            return False
        if self.a + self.c < self.b:
            return False
        if self.b + self.c < self.a:
            return False
        return True
    
    def is_right(self):
        if self.a**2 + self.b**2 == self.c**2:
            return True
        if self.a**2 + self.c**2 == self.b**2:
            return True
        if self.b**2 + self.c**2 == self.a**2:
            return True
        return False

if __name__ == '__main__':
    t = Triangle(1,3,5)
    print(t.is_valid())
    print(t.is_right())

    t = Triangle(3,4,5)
    print(t.is_valid())
    print(t.is_right())