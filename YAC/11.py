# loops -> for, while

# count = 1
# while True : 
#     print("Hellow")
#     count = count + 1
#     if(count > 5) :
#         break


count = 1
while count<=5 : 
    print("Hellow")
    count += 1


li = (1,2,3,4,5,6)
i = 0
x = 4
while i<len(li):
    if(x == li[i]):
        print(x, "is found at idx",i)
        break
    i += 1



li = [1,2,3,4,5,7,8]
for el in li:
    print(el)
tup = (1,2,3,4,5,7,8)
for el in tup:
    print(el)
str = "Apna College"
for el in str:
    print(el)
else:
    print("End")


#range function (Very imp function)
# start = 0(by default)
# step = 1(by default)
# stop = user_defined
# range(start, stop+1, step)
print(range(3))     # stop
print(range(3,9))   # start stop
print(range(3,9,2)) # start stop step
for el in range(3,10,2): 
    print(el)



sequence = range(2,10,2)
print(sequence[0])
print(sequence[1])
print(sequence[2])
print(sequence[3])
for el in sequence:
    print(el)

#print 1 to 100
for el in range(101):
    print(el)

#print 100 to 1
for el in range(100,0,-1):
    print(el)


n = int(input("Enter n: "))
# for el in range(n,n*10+1,n):
#     print(el)
# OR
# for el in range(1,11):
#     print(el*n)