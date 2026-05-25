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
