li = ["moksh", "het"]

d2 = {"karan" : 90, "sahil" : 40}

print(d2)
# d2 = d2.fromkeys(li)

d2.setdefault("karan",9)
print(d2)


collection = {1,2,3,4,5}
collection.add(6)
print(collection)
collection.remove(6)
print(collection)
collection.discard(99)
print(collection)




x = {1,2,3,4}
y = {3,4,5,6}
res = x.symmetric_difference(y)
print(res)







def test():
    print("Hello World")
    return 200

x = test
print(x)



def add(a,b):
    print("addition function called...")
    print(a+b)
    
    
add(True,100)




def getUserData(age, salary, name):
    print(f"Age = {age}")
    print(f"Salary = {salary}")
    print(f"Name = {name}")
    
    
print("===========")
# getUserData(age=20,name="Karan",salary=30000)
getUserData(20,name="Karan",salary=30000)
getUserData(20,"Karan",salary=30000)
