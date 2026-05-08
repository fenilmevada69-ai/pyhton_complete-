try:
    num = int(input("Enter a number: "))
    print(num)
except TypeError as e:
    print("Type Error: Pls enter valid number")
    print(e)
except ValueError as e:
    print("Value Error: Pls enter valid number")
    print(e)
except ZeroDivisionError as e:
    print("ZeroDivision Error: Pls enter valid number")
    print(e)
except Exception as e:
    print("Exception: Pls enter valid number")
    print(e)
    
print("Tank you")




a = int(input("Enter a: "))
b = int(input("Enter b: "))

if(b == 0):
    raise myZeroError("Hey pls enter valid value of b")
else:
    print(a/b)