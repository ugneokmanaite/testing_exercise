import math

class Calc:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

    def sqrt(self, num1):
        return math.sqrt(num1)

    def ceil(self, num1):
        return math.ceil(num1)

simple_calc = Calc()

