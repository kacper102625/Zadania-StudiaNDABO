class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Nie można dzielić przez zero!")
        return a / b
# funkcja 
def calculate_expression():
    calc = Calculator()          
    result = calc.add(10, 5)     
    result = calc.subtract(result, 3)
    result = calc.multiply(result, 2)
    result = calc.divide(result, 4)
    return result


