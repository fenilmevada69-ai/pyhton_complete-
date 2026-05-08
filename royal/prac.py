# def greet(fx):
#     def inner(name):
#         if(name == 'Fenil'):
#             print("Hello Fenil How are you!")
#         else:
#             print("Invalid name")
#     return inner






# def login_required(func):
#     if(func.__name__ == "access_data"):
#         def mfx(role):
#             if role == "ADMIN":
#                 func(role)
#             else:
#                 print("You cant able to acces it!")
#         return mfx
#     elif(func.__name__ == "access_files"):
#         def mfx(role):
#             if role == "ADMIN" or role == "MANAGER":
#                 func(role)
#             else:
#                 print("You cant able to acces it!")
#         return mfx

# @login_required
# def access_data(role):
#     print(f"accessing data and my role is {role}")

# @login_required
# def access_files(role):
#     print(f"accessing files and my role is {role}")
    
# access_data("ADMIN")
# access_data("MANAGER")
# access_files("ADMIN")
# access_files("USER")
# access_files("MANAGER")






# def access_cartpages(*args, **kwargs):
#     print("accessing cart pages by", kwargs.get("role"))
#     print("accessing cart pages")

# def login_riquired(fx):
#     def mfx(*args, role):
#         if role in args:
#             print("authoried access!")
#             fx(args, role=role)
#         else:
#             print("unauthorized access!")        
#     return mfx
        
# @login_riquired
# def access_cartpages(*args, role):
#     print("accessing cart pages by", role)

# access_cartpages("user", "admin", role="user")




# def authentication(fx):
#     def mfx(name, **kwargs):
#         if kwargs.get("age") and kwargs.get("course"):
#             if kwargs.get("age") < 18:
#                 print("admission not granted for", name, "age is less than 18")
#             else:
#                 print("admission granted for", name)
#                 fx(name, **kwargs)
#         else:
#             print("admission not granted for", name, "age or course is missing")
#     return mfx
        
# def admission(name, **kwargs):
#     print("admission process for", name, "with details", kwargs)


# admission("raj",age=19,course="IT") #valid
# admission("parth",age=16,course="CS") #not valid age <18
# admission("jay",course="IT") #not valid age is not present
# admission("amit") #not valid both age and course not present
# admission("kunal",age=22) #not valid course not present




# def authentication(func):
#     def mfx(*args,role):
#         if role in args:
#             print("authorised access!")
#         else:
#             print("unauthorised access!")
#     return mfx    
# @authentication
# def access_cartpages(*args,role):
#     print("accessing cart pages: ", role)
# access_cartpages("user", "admin", role="user")




