li1 = [1,2,3,2]
li2 = [4,5,6]

li1.extend(li2)

print(li1)
print(li2)

li1.reverse()
print(li1)

print(li1)
li1.remove(2)
print(li1)

print(li1)
print(li2)
li1.copy()
print(li1)
print(li2)


li = [1,2,3,4,5,6,7]
print(li[::-1])
print(li[3:-5:-1])



a = [1,2,3]
b = a


print(a,b)
b += [1,2,3]
print(a,b)



tuple = (2)
print(tuple)