#Part 1 BMI Calculator
def bmi(weight: float, height: float):
    return weight/height**2

#Part 2 Divide two numbers
def divide(num1: int, num2: int):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("Error: Division by zero.")
        return None
#Part 3 File IO

#Part 4 Dictionaries

#Part 5 List Loop
