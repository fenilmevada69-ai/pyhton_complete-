age = 19
print(age)
def changeAge():
    global age
    age = 21
print(age)

def outer():
    x = 10
    def inner():
        nonlocal x
        x = 20
    inner()
    print(x)
outer()


def add(*args):
    return sum(args)
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum+1
print(add(1,2,3))
print(add(1,2,3,4))
print(add(1,2,3,4,5))

# it takes key value as argument
# def d1(**kargs):
#     for i,j in kargs.items():
#         print(f"{i} : {j}")
# def d1(**kargs):
#     for i in kargs.keys():
#         print(f"{i} --> {kargs[i]}")
# d1(name="moksh" , age=20 , gender="male")


def d1(**kargs):
    for i,j in kargs.items():
        print(f"{i} : {j}")
d1(name="moksh" , age=20, gender="male")








data = ()
print(type(data))
print(type(data).__name__)