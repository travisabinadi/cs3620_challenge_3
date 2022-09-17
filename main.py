# Challenge 3
# Travis Smith

# Part 1
# Assume you want to build two functions for discounting products on a website.
# Function number 1 is for student discount which discounts the current price by 10%.
# Function number 2 is for an additional discount for regular buyers which discounts an additional 5% on the current student discounted price.
# Depending on the situation, we want to be able to apply both discounts on the products.
# Design the above two mentioned functions and apply them both simultaneously on the price.
from Computer import Computer
from Desktop import Desktop
from Laptop import Laptop
from Number import Number


def apply_discount(cost: float, is_student_discount: bool, is_additional_discount: bool) -> float:
    """
    Apply a discount based on which they qualify for.
    STUDENT_DISCOUNT: 10 percent discount applied
    ADDITIONAL_DISCOUNT: 5 percent additional discount for student buyers
    :return: discounted value
    """
    new_cost = cost
    if is_student_discount and is_additional_discount:
        new_cost = additional_discount(student_discount(cost))
    elif is_additional_discount:
        new_cost = student_discount(new_cost)
    return new_cost


def student_discount(cost: float) -> float:
    return cost - (cost * 0.1)


def additional_discount(cost: float) -> float:
    return cost - (cost * 0.05)


# Part 2
# Calculate the value of mathematical expression x*(x+5)^2 where x= 5 using lambda expression.
lamb = lambda x: x * (x + 5) ** 2


# Part 3
# Consider a list in Python which includes prices of all the items in a store.
# Build a function to discount the price of all the products by 10%.
# Use a map to apply the function to all the elements of the list so that all the product prices are discounted.
def discount_items(item_costs: list[float]) -> list[float]:
    return [student_discount(item_cost) for item_cost in item_costs]
    # Also could be this if we need to use lambda, but I find the above one more readable
    return list(map(lambda item_cost: student_discount(item_cost), item_costs))

# Part 4 in project other files

# Part 5
# Using the concept of operator overloading in Python, change the behavior of the multiplication operator in a way that multiplication operator behaves like an addition operator.


### Main ###
print("Part 1:")
cost = 99.99
discounted_cost = apply_discount(cost, True, True)
print(discounted_cost)

print("\nPart 2:")
print(lamb(5))

print("\nPart 3:")
items = [0.99, 1.99, 55.55, 7.77, 100.01, 10.00]
items = discount_items(item_costs=items)
[print(item) for item in items]

print("\nPart 4:")
Computer(memory="8 GB", cpu="Intel Core i5", weight="13.14 pounds").displayspecs()
Laptop(memory="16 GB", cpu="Radeon RX 6800M", weight="5.29 pounds", battery="Lithium-ion polymer").displayspecs()
Desktop(memory="16 GB", cpu="12th Gen Intel® Core™ i7", weight="", graphics_card="").displayspecs()

print("\nPart 5:")
num1 = Number(2)
num2 = Number(3)
print(f"2 * 3 = {num1 * num2}")
