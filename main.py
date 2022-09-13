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
def file_io():
    file = open("demo.txt", "w")
    file.write("Some random data")
    file.close()
    file = open("demo.txt", "r")
    contents = file.readlines()
    for line in contents:
        print (line)
    file.close()
    file = open("demo.txt", "a")
    file.write("\nYay! I have been added!")
    file.close()

#Part 4 Dictionaries
def get_price(product_name: str) -> float:
    products = {
        "Apple": 10,
        "Orange": 20,
        "Pear": 30.99,
        "Mango": 50.55,
        "Raspberries": 9999.99
    }
    if product_name in products.keys():
        return products[product_name]
    else:
        print("That item is currently unavailable :( Try back later.")

#Part 5 List Loop
def list_loop():
    nums = [num for num in range(0, 100)]
    for num in nums:
        if num % 2 == 1:
            print(num)

### Main ###
print(f"My BMI is {bmi(77, 1.79832)}.")
print(f"20 divided by 4 is {divide(20, 4)}")
file_io()
print(f"A Mango costs ${get_price('Mango')}.")
list_loop()
