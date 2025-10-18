"""
WELCOME TO PYTHON LEARNING!
===========================
This file contains interactive examples and exercises to help you learn Python.
Run this file to see the output, then modify the code to experiment and learn!

To run: Click the "Run" button above or the workflow will start automatically.
"""

print("=" * 50)
print("WELCOME TO PYTHON LEARNING!")
print("=" * 50)
print()

# =============================================================================
# SECTION 1: VARIABLES AND DATA TYPES
# =============================================================================
print("\n--- SECTION 1: Variables and Data Types ---")

# Variables store data
name = "Alice"
age = 25
height = 5.6
is_student = True

print(f"Name: {name} (type: {type(name).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Height: {height} (type: {type(height).__name__})")
print(f"Is Student: {is_student} (type: {type(is_student).__name__})")

# TRY IT: Create your own variables below
# your_name = "Your Name Here"
# your_age = 0
# print(f"Hello, my name is {your_name} and I am {your_age} years old")


# =============================================================================
# SECTION 2: BASIC OPERATIONS
# =============================================================================
print("\n--- SECTION 2: Basic Operations ---")

# Arithmetic operations
a = 10
b = 3
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b} (integer division)")
print(f"{a} % {b} = {a % b} (remainder)")
print(f"{a} ** {b} = {a ** b} (power)")

# TRY IT: Practice arithmetic
# result = 5 * 6 + 10
# print(f"My calculation: {result}")


# =============================================================================
# SECTION 3: STRINGS
# =============================================================================
print("\n--- SECTION 3: Strings ---")

message = "Hello, Python!"
print(f"Original: {message}")
print(f"Uppercase: {message.upper()}")
print(f"Lowercase: {message.lower()}")
print(f"Length: {len(message)} characters")
print(f"First character: {message[0]}")
print(f"Last character: {message[-1]}")
print(f"Slice (0-5): {message[0:5]}")

# String concatenation
greeting = "Hello"
person = "World"
full_greeting = greeting + ", " + person + "!"
print(f"Concatenation: {full_greeting}")

# TRY IT: Create and manipulate your own strings
# favorite_food = "pizza"
# print(f"I love {favorite_food.upper()}!")


# =============================================================================
# SECTION 4: LISTS (Arrays)
# =============================================================================
print("\n--- SECTION 4: Lists ---")

# Lists store multiple items
fruits = ["apple", "banana", "cherry", "date"]
print(f"Fruits: {fruits}")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Number of fruits: {len(fruits)}")

# List operations
fruits.append("elderberry")
print(f"After append: {fruits}")

fruits.remove("banana")
print(f"After remove: {fruits}")

# List slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Numbers: {numbers}")
print(f"First 5: {numbers[:5]}")
print(f"Last 3: {numbers[-3:]}")
print(f"Every 2nd: {numbers[::2]}")

# TRY IT: Create your own list
# my_hobbies = ["reading", "gaming", "coding"]
# my_hobbies.append("music")
# print(my_hobbies)


# =============================================================================
# SECTION 5: DICTIONARIES (Key-Value Pairs)
# =============================================================================
print("\n--- SECTION 5: Dictionaries ---")

# Dictionaries store key-value pairs
person_info = {
    "name": "Bob",
    "age": 30,
    "city": "New York",
    "occupation": "Developer"
}

print(f"Person: {person_info}")
print(f"Name: {person_info['name']}")
print(f"Age: {person_info['age']}")

# Adding/updating items
person_info["email"] = "bob@example.com"
person_info["age"] = 31
print(f"Updated: {person_info}")

# Dictionary methods
print(f"Keys: {list(person_info.keys())}")
print(f"Values: {list(person_info.values())}")

# TRY IT: Create a dictionary about yourself
# my_info = {"name": "Your Name", "favorite_color": "blue"}
# print(my_info)


# =============================================================================
# SECTION 6: CONTROL FLOW - IF/ELSE
# =============================================================================
print("\n--- SECTION 6: Control Flow (if/else) ---")

temperature = 75

if temperature > 80:
    print("It's hot outside!")
elif temperature > 60:
    print("It's a nice day!")
else:
    print("It's cold outside!")

# Comparison operators: ==, !=, <, >, <=, >=
number = 15
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# TRY IT: Write your own if/else statement
# score = 85
# if score >= 90:
#     print("Grade: A")
# elif score >= 80:
#     print("Grade: B")
# else:
#     print("Grade: C or below")


# =============================================================================
# SECTION 7: LOOPS
# =============================================================================
print("\n--- SECTION 7: Loops ---")

# For loop with range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(f"  {i}")

# For loop with list
colors = ["red", "green", "blue"]
print("Colors:")
for color in colors:
    print(f"  {color}")

# While loop
count = 1
print("While loop countdown:")
while count <= 3:
    print(f"  Count: {count}")
    count += 1

# TRY IT: Practice loops
# for i in range(10, 0, -1):
#     print(f"Countdown: {i}")


# =============================================================================
# SECTION 8: FUNCTIONS
# =============================================================================
print("\n--- SECTION 8: Functions ---")

# Function definition
def greet(name):
    """This function greets a person"""
    return f"Hello, {name}!"

# Function call
result = greet("Charlie")
print(result)

# Function with multiple parameters
def add_numbers(x, y):
    """Add two numbers and return the result"""
    return x + y

sum_result = add_numbers(10, 20)
print(f"10 + 20 = {sum_result}")

# Function with default parameters
def introduce(name, age=18):
    return f"My name is {name} and I'm {age} years old"

print(introduce("David"))
print(introduce("Emma", 25))

# TRY IT: Create your own function
# def multiply(a, b):
#     return a * b
# 
# print(multiply(5, 7))


# =============================================================================
# SECTION 9: LIST COMPREHENSIONS (Advanced but useful!)
# =============================================================================
print("\n--- SECTION 9: List Comprehensions ---")

# Traditional way
squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(f"Squares (traditional): {squares}")

# List comprehension way (more concise)
squares_comp = [i ** 2 for i in range(1, 6)]
print(f"Squares (comprehension): {squares_comp}")

# With condition
even_numbers = [i for i in range(1, 11) if i % 2 == 0]
print(f"Even numbers 1-10: {even_numbers}")


# =============================================================================
# PRACTICE EXERCISES
# =============================================================================
print("\n" + "=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)
print("""
Uncomment and complete these exercises below to practice!

EXERCISE 1: Variables
---------------------
Create variables for your favorite movie, year it was released,
and rating (out of 10). Print them in a nice formatted message.

# movie = "Your Movie"
# year = 2020
# rating = 9.5
# print(f"My favorite movie is {movie} ({year}), rating: {rating}/10")


EXERCISE 2: Lists
-----------------
Create a list of 5 numbers, then:
- Add a new number to the list
- Remove the first number
- Print the sum of all numbers
- Print the average

# numbers = [10, 20, 30, 40, 50]
# numbers.append(60)
# numbers.remove(10)
# total = sum(numbers)
# average = total / len(numbers)
# print(f"Sum: {total}, Average: {average}")


EXERCISE 3: Functions
---------------------
Write a function that takes a temperature in Celsius
and converts it to Fahrenheit. Formula: F = C * 9/5 + 32

# def celsius_to_fahrenheit(celsius):
#     return celsius * 9/5 + 32
#
# temp_c = 25
# temp_f = celsius_to_fahrenheit(temp_c)
# print(f"{temp_c}°C = {temp_f}°F")


EXERCISE 4: Loops and Conditions
---------------------------------
Write a loop that prints numbers 1-20, but:
- For multiples of 3, print "Fizz"
- For multiples of 5, print "Buzz"
- For multiples of both, print "FizzBuzz"

# for i in range(1, 21):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
""")

print("\n" + "=" * 50)
print("Happy Learning! Modify this file and re-run it to practice!")
print("=" * 50)
