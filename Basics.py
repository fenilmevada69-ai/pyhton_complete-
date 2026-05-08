##01
h1 = [1,2,3]
h2 = h1[:]  # this is only copy
h1[0] = 55
print(h1)
print(h2)

import copy 
h1 = [1,2,3, [99,88], 4]
h2 = copy.deepcopy(h1)
h1[0] = 55
h1[3][0] = 111
print(h1)
print(h2)




##02
l1 = [1,2,3]
l2 = l1
l1[0] = 55
print(l2)

p1 = [1,2,3]
p2 = p1
p1[0] = 55
print(p2)   ##this is only bcs lists are mutable




##03
print(0o20)     #for octal
print(0x20)     #for hex
print(0b1000)   #for binary
#dont use this

#use inbiuld methods
print(oct(64))  
print(hex(64))
print(bin(64))

#or use direct int
print(int("64",8))
print(int("64",16))
print(int("1000",2))





##04
print((0.1 + 0.1 + 0.1) - 0.3)
#use modules
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))
from fractions import Fraction
myFrac = Fraction(2,7)
print(myFrac)




##05
setone = {1,2,3,4}
print(setone & {1,3})
print(setone | {1,3})
print(setone - {1,2,3,4})
print(True == 1)
print(False == 0)
print(True is 1)
print(False is 0)
print(True + 4)




##06 
quantity = 2
chai = "Masala"
s = "I ordered {} cups of {} chai"
print(s.format(quantity,chai))




##07
tea_varity = ["Black", "Green", "Oolong", "White"]
print(tea_varity[1:2])
tea_varity[1:2] = "Lemon"
print(tea_varity)   #problem
tea_varity = ["Black", "Green", "Oolong", "White"]
tea_varity[1:2] = ["Lemon"]
print(tea_varity)
tea_varity[1:3] = ["green", "Masala"]
print(tea_varity) 
print(tea_varity[1:1])
tea_varity[1:1] = ["test", "test"]
print(tea_varity) 
tea_varity[1:3] = []    #insert nothing is one type of deletion
print(tea_varity)   




##07
squered_num = {x:x**2 for x in range(6)}
print(squered_num)



##08
tea_types = ("Black", "Green", "Oolong")
(a,b,c) = tea_types
print(a)
print(b)




##09
print("a"*5)
print(5*"a")




##10
import math
def circle(radius):
    area = math.pi * radius**2
    circum = 2 * math.pi * radius
    return area, circum

a,c = circle(4)
print(a)
print(c)




##11
li = [1,2,3,4]
I = iter(li)
print(hex(id(li[0])))
print(I)    #iterator object (gives address of iteartor)
print(hex(id(li[0])))
print(hex(id(next(I))))
print(next(I))
print(next(I))
print(next(I))

li = [1,2,3,4,5,6]
I = iter(li)
### next(I) == I.__next__() both are same
try:
    print(next(I))
    print(I.__next__()) 
    print(next(I))
    print(next(I))
    print(next(I))
    print(next(I))
except Exception as e:
    print("Exception")
finally:
    print("Finally")
    
    
    
    
    
##12
def cube(a):
    return a**3
print(cube(3)) #use this method if u have to use add function 1000 times
                #but use lambda if u have to use add function only once

cube = lambda x:x**3    #lambda is used more in django and flasks.. 
print(cube(3))






##13
def even(limit):
    for i in range(2,limit,2):
        yield i

# yeild stores the state and function...
for num in even(10):
    print(num)
    
    



##14
#closure
s = 99
def f1():
    s = 88
    def f2():
        print(s)
    return f2

myResult = f1()
myResult()