# str = "Hello World!"
# print(str.endswith("!"))
# print(str.capitalize())
# print(str.upper())
# print(str.lower())
# print(str.replace("e", "b"))
# print(str.replace("Hell", "Apa"))
# print(str.find("World!"))
# print(str.count("World!"))
# print(str.partition("is"))
# print(str.rpartition("is"))








# Normal Method
# str = input("Enter your post: ")
# if("harry" in str):
#     print("harry is present")
# else:
#     print("harry is not present")
#Advance Program
str = input("Enter your post: ")
if("harry".lower() in str.lower()):
    print("harry is present")
else:
    print("harry is not present")
    
    
    
    
email = "   samirvithalani.com   "
print(email.upper())
print(email.lower())
print(email.capitalize())
print(email.swapcase())
print(email.title())
print(email.strip())
print(email.lstrip())
print(email.rstrip())
email = "java12"
print(email.isalnum())  #spaces not allowed(either alpha or num or both)
email = "java h"
print(email.isalpha())  #spaces not allowed(only alpha)
email = "12 4"
print(email.isnumeric()) #spaces not allowed(only numeric)
email = "5lower email"
print(email.islower())
email = "5lower email".upper()
print(email.isupper())







#boolean

data = ""

flag = data.startswith("j")
print(flag)
print('endswith',data.endswith("a"))
print("isalnum",data.isalnum())
print("alpha...",data.isalpha())
print("numric..",data.isnumeric())
#print(data.isdigit())
print("lower",data.islower()) #"abcd" #"abcd1" # "abc " # "Abc"
print("upper",data.isupper())
print("isspace",data.isspace()) #" "
print("is title",data.istitle()) #
print(data.isprintable()) # \n 




data = "javascripta"
data = data.replace("a", "#", 3)
print(data)