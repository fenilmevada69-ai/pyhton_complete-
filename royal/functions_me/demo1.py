def getUserData(x, **kwargs):
    print("kwargs", kwargs)
    print("x", x)

getUserData(10, name="royal", age=20, salary=2000)