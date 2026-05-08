# modules
import random   # random module

# n=10

# while True:
#     num = random.randint(1,100)
#     print(num)
#     if(num == n):
#         break
    
    
    
    
#imp random functions

# random.random()       [0,1)
# random.randint(min,max)    [min,max]  
# random.randrange(start,stop,step) similar to range
# random.choice(["red", "green", "yellow"])
# li = [1,2,3,4,5]
# random.shuffle(li)    #works only with list only and only     
# random.sample(li,k)   # returns list of k elements no repeatation


# c = range(10)
# print(type(c))



import string
# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
wholeString = string.ascii_letters + string.digits + string.punctuation
print(wholeString)
passWord = ""
# print(random.sample(wholeString,10))
for i in range(1,13):
    rand = random.choice(wholeString)
    passWord += rand
print(passWord)
print(len(passWord))

# other method list comprehension[function for i in range]
res = [random.choice(wholeString) for i in range(1,13)]
res = "".join([random.choice(wholeString) for i in range(1,13)])
print(res)
print(len(res))

r = "".join(random.sample(wholeString,12))
print(r)
print(len(r))



# import random as r
# num = r.random()
# print(num)


# from random import randint
# print(randint(100,1000))



import math as m
print(m.sqrt(29))
print(m.pow(3,4))
print(m.factorial(6))
print(m.e)
print(m.pi)
print(m.fsum([1,2,3,4,5]))
print(m.floor(45.88))