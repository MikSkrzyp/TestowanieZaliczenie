class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Cannot divide by zero"
        return a // b

    def power(self, a, b):
        return a ** b

    def square(self, a):
        return a * a

    def cube(self, a):
        return a * a * a

    def absolute(self, a):
        return abs(a)

    def sqrt(self, a):
        if a < 0:
            return "Error: Cannot take the square root of a negative number"
        return int(a ** 0.5)

    def mod(self, a, b):
        if b == 0:
            return "Error: Cannot mod by zero"
        return a % b
