users =["amit","sumit","raj","parth","jay","sneha","kunal","priyanka","karina"]

#if
userswithlen = {i:len(i) for i in users if len(i)>4}
print(userswithlen)


names = ["radar", "level", "hello", "world", "madam"]
nameswithpalin = {i:"palindrome" if i == i[::-1] else "not palindrome" for i in names}
print(nameswithpalin)


userwithinitial = {i[0]:i for i in users}
print(userwithinitial)