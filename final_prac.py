# =========================================================
# PYTHON ALL-IN-ONE PRACTICE FILE
# Covers Most Important Python Concepts
# =========================================================

# =========================================================
# 1. PRINT & COMMENTS
# =========================================================

print("Hello Python")

# This is a single line comment

"""
This is
multi-line comment
"""

# =========================================================
# 2. VARIABLES & DATA TYPES
# =========================================================

name = "Fenil"         # string
age = 20               # integer
height = 5.8           # float
is_student = True      # boolean
complex_num = 2 + 3j   # complex

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(complex_num))

# =========================================================
# 3. TYPE CASTING
# =========================================================

a = "100"

print(int(a))
print(float(a))
print(str(200))

# =========================================================
# 4. OPERATORS
# =========================================================

x = 10
y = 3

# Arithmetic
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)
print(x % y)
print(x ** y)

# Comparison
print(x > y)
print(x < y)
print(x == y)

# Logical
print(True and False)
print(True or False)
print(not True)

# Membership
text = "Python"
print("P" in text)

# Identity
a = [1, 2]
b = a
print(a is b)

# =========================================================
# 5. INPUT
# =========================================================

# name = input("Enter name: ")
# print(name)

# =========================================================
# 6. CONDITIONAL STATEMENTS
# =========================================================

num = 10

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# Ternary Operator
age = 19
ans = "Adult" if age >= 18 else "Minor"
print(ans)

# =========================================================
# 7. LOOPS
# =========================================================

# FOR LOOP
for i in range(5):
    print(i)

# WHILE LOOP
count = 0

while count < 5:
    print(count)
    count += 1

# break
for i in range(10):
    if i == 5:
        break
    print(i)

# continue
for i in range(5):
    if i == 2:
        continue
    print(i)

# pass
for i in range(3):
    pass

# =========================================================
# 8. STRINGS
# =========================================================

text = "Python Programming"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())

print(text.find("Pro"))
print(text.replace("Python", "Java"))

print(text.startswith("Py"))
print(text.endswith("ing"))

print(text.split())
print("-".join(["a", "b", "c"]))

print(text[0])
print(text[-1])
print(text[0:6])
print(text[::-1])

# String Checking Methods
print("123".isdigit())
print("abc".isalpha())
print("abc123".isalnum())
print("   ".isspace())

# f-string
name = "Fenil"
print(f"My name is {name}")

# =========================================================
# 9. LISTS
# =========================================================

li = [10, 20, 30, 40]

print(li)

li.append(50)
li.insert(1, 100)
li.remove(30)
li.pop()

print(li)

print(li[0])
print(li[-1])
print(li[1:3])

# Loop through list
for item in li:
    print(item)

# List comprehension
square = [x*x for x in range(5)]
print(square)

# =========================================================
# 10. TUPLES
# =========================================================

tup = (1, 2, 3, 4)

print(tup)
print(tup[0])

# Packing & Unpacking
a, b, c, d = tup
print(a, b, c, d)

# =========================================================
# 11. SETS
# =========================================================

s = {1, 2, 3, 4}

s.add(5)
s.remove(2)

print(s)

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# =========================================================
# 12. DICTIONARIES
# =========================================================

student = {
    "name": "Fenil",
    "age": 20,
    "course": "Python"
}

print(student)

print(student["name"])

student["age"] = 21
student["city"] = "Ahmedabad"

print(student.keys())
print(student.values())
print(student.items())

# Loop in dictionary
for key, value in student.items():
    print(key, value)

# fromkeys()
keys = ("a", "b", "c")
new_dict = dict.fromkeys(keys, 0)
print(new_dict)

# =========================================================
# 13. FUNCTIONS
# =========================================================

def greet():
    print("Hello")

greet()

# Function with parameters
def add(a, b):
    return a + b

print(add(10, 20))

# Default arguments
def intro(name="Guest"):
    print("Welcome", name)

intro()
intro("Fenil")

# Arbitrary arguments
def total(*nums):
    print(sum(nums))

total(1, 2, 3, 4)

# Keyword arguments
def details(**data):
    print(data)

details(name="Fenil", age=20)

# Lambda function
square = lambda x: x*x
print(square(5))

# =========================================================
# 14. RECURSION
# =========================================================

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# =========================================================
# 15. EXCEPTION HANDLING
# =========================================================

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("Finished")

# =========================================================
# 16. FILE HANDLING
# =========================================================

# Writing file
with open("demo.txt", "w") as f:
    f.write("Hello Python")

# Reading file
with open("demo.txt", "r") as f:
    print(f.read())

# =========================================================
# 17. OOP (OBJECT ORIENTED PROGRAMMING)
# =========================================================

class Student:

    school = "ABC School"   # class variable

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

obj = Student("Fenil", 20)

obj.display()

# Inheritance
class Person:
    def speak(self):
        print("Speaking")

class Teacher(Person):
    def teach(self):
        print("Teaching")

t = Teacher()

t.speak()
t.teach()

# =========================================================
# 18. MODULES
# =========================================================

import math

print(math.sqrt(25))
print(math.factorial(5))

# =========================================================
# 19. DATE & TIME
# =========================================================

import datetime

today = datetime.datetime.now()

print(today)

# =========================================================
# 20. RANDOM
# =========================================================

import random

print(random.randint(1, 10))

# =========================================================
# 21. ENUMERATE & ZIP
# =========================================================

names = ["A", "B", "C"]

for index, value in enumerate(names):
    print(index, value)

a = [1, 2, 3]
b = ["x", "y", "z"]

print(list(zip(a, b)))

# =========================================================
# 22. MAP, FILTER, REDUCE
# =========================================================

nums = [1, 2, 3, 4]

mapped = list(map(lambda x: x*2, nums))
print(mapped)

filtered = list(filter(lambda x: x % 2 == 0, nums))
print(filtered)

from functools import reduce

result = reduce(lambda x, y: x + y, nums)
print(result)

# =========================================================
# 23. ITERATORS
# =========================================================

nums = [10, 20, 30]

it = iter(nums)

print(next(it))
print(next(it))

# =========================================================
# 24. GENERATORS
# =========================================================

def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()

print(next(g))
print(next(g))

# =========================================================
# 25. DECORATORS
# =========================================================

def decorator_func(func):

    def wrapper():
        print("Before function")
        func()
        print("After function")

    return wrapper

@decorator_func
def hello():
    print("Hello")

hello()

# =========================================================
# 26. REGEX
# =========================================================

import re

text = "My number is 9876543210"

result = re.findall(r"\d+", text)

print(result)

