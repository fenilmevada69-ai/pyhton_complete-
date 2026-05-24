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

    
    
email = "FMEADA86@GMAIL.COM"
print(email.swapcase()) 


name = "    iamfenilmevada    "
print(name.title())
print(name.strip())
print(name.strip().isalnum())


name = "hello World!"
print(name.rpartition("lo"))


text = " hel    lo"
# print(text.rpartition("-"))


print(text.isspace())



data = "javascriptaga"
data = data.replace("a", "#", 3)
print(data)


text = "a,b,c"
print(text.rsplit(","))


name = "i am fenil mevada"
print(name.capitalize())
print(name.title())