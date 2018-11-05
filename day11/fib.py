# 0 1 1 2 3 5 8 13

class Fib:
    def __init__(self, n):
        self.a = 0
        self.b = 1
        self.max = n

    def __iter__(self):
        return self

    def __next__(self):
        while self.a <= self.max:
            c = self.a
            self.a = self.b
            self.b += c
            return self.a

        raise StopIteration()


f = Fib(10)
print(f)

for i in Fib(10):
    print(i)
