class Complex(object):
    # Complex(2,4) + Compex(1,3) = Complex(3,7)
    def __init__(self, c_real, c_imaginary):
        self.real = c_real
        self.imaginary = c_imaginary

    def __str__(self):
        return f"{self.real}+{self.imaginary}i"

    def __add__(self, other):
        r = self.real + other.real
        i = self.imaginary + other.imaginary
        return Complex(r, i)

    def __sub__(self, other):
        r = self.real - other.real
        i = self.imaginary - other.imaginary
        return Complex(r, i)

    def __mul__(self, other):
        r = self.real * other.real - self.imaginary * other.imaginary
        i = self.imaginary * other.real + self.real * other.imaginary
        return Complex(r, i)

    def __pow__(self, power, modulo=None):
        if power == 2:
            return self * self


a = Complex(1, 2)
b = Complex(3, 4)
print(a + b)
print(a - b)
print(a * b)
print(a **2)
# print("{}+{}i".format((a + b).real, (a + b).imaginary))
