li = [1,2,3,4,9,7]
print(min(li))
print(max(li))
print(sum(li))
print(sorted(li,reverse=True))
print(len(li))


l = [10,20,30]
li.extend(l)
print(li)
li.append(99)
print(li)
li.remove(99)
print(li)
li.pop()
print(li)
li.insert(2,88)
print(li)


# li = ["raj", "shyam", "kunt", "anujara"]
# li.sort(key=len)
# print(li)
print(li.count(88))
print(li.index(88))
print(li)
li.clear()
print(li)


a = [1,2,3]
b = a.copy()
print(a)
print(b)
b = b.extend([3,4,5])
print(a)
print(b)



# c = [1,2,3,4,5,6]
# a, b, d = c
# print(a,b,d)




li = [10, 20, 30, 40]
a, b, c, d = li
print(li)
print(a)
print(b)
print(c)
print(d)
a, b, *c = li
print(li)
print(a)
print(b)
print(c)
# it is known as unpacking of list(like destructuring in js)