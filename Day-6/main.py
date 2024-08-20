def greet():
    print("Hello, Aditya!")
greet()

# Calling the function with different arguments
def greet1(name):
    print(f"Hello, {name}!")
greet1("Alice")
greet1("Bob")

# Function with a Return Value
def add(a, b):
    return a + b
result = add(5, 7)
print(result)

# Function with Default Parameters
def greet2(name="Aditya"):
    print(f"Hello, {name}!")
greet2()  
greet2("Roshan")

# Function with Multiple Return Values
def get_min_max(numbers):
    return min(numbers), max(numbers)
min_val, max_val = get_min_max([2, 5, 1, 9, 4])
print(f"Min: {min_val}, Max: {max_val}")

# Using *args and **kwargs
def print_numbers(*args):
    for number in args:
        print(number)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_numbers(1, 2, 3, 4)  
print_info(name="Alice", age=30)

# while loop with else statement
count = 0
while count < 3:
    print(f"Count is {count}")
    count += 1
else:
    print("Loop completed without a break.")