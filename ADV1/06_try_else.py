try:
    a = int(input("Enter num only: "))
except Exception as e:
    print(e)
else:
    print("I am else, only comes when try is executed successfully")