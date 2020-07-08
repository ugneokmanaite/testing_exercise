# importing math module
import math

# creating calculator class
class Calc:

# creating functions for the calculator
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

# creating an objective
simple_calc = Calc()

