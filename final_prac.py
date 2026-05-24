str = "Hello World!"


print(str.endswith("!"))
print(str.startswith("H"))
print(str.capitalize())
print(str.upper())
print(str.lower())
print(str.replace("Hello", "Wordl"))
print(str.find("ello"))
print(str.count("ello"))
print(str.partition("ello"))



str = input("Enter text: ")
if("harry" in str.lower()):
    print("Harry is preset!")
else:
    print("Harry is not present!")
    
    
email = "FMEADA86@GMAIL.COM"
print(email.swapcase()) 