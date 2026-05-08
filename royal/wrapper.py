# def hello():
#     print("hello")

# def wrapper(func):
#     print("Extra Work..")
#     func()

# wrapper(hello)




# def hello():
#     print("hello")

# def wrapper(func):
#     def inner():
#         print("Extra Work..")
#         func()
#     return inner

# hello = wrapper(hello)
# hello()





# def wrapper(func):
#     def inner():
#         print("Extra Work..")
#         func()
#     return inner

# @wrapper
# def hello():
#     print("hello")

# hello()






def wrapper(func):
    def inner():
        print("Extra Work..")
        func()
    return inner

def hello():
    print("hello")

# choose when to decorate
wrapped = wrapper(hello)


hello()
wrapped()