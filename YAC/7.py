# Lists and tuples(Similar to arrays)
# Lists are muttable in python
marks = [1,2,3,4,5,6,7,8]
print(marks[0])
print(marks[2])
print(marks)
marks[0] = 99
print(marks)
# sublist similar to substring
print(marks[1:4])
print(marks[4:len(marks)])


li1 = [1,2,3]
li2 = [4,5,6]
li1.extend(li2)
print(li1)


li = [7,2,3]
li.append(4)
print(li)
li.sort()
print(li)
li.sort(reverse=True)
print(li)
li.reverse()
print(li)
li.insert(2,99)
print(li)
li.remove(2)    #remove first occurance of element
print(li)
li.pop(2)       #remove element at idx 
print(li)
newli = li.copy()




li = [1,10,5,4,3,2,7,9,6,11,10,12,8]
print(sorted(li))
print(sorted(li,reverse=True))

#only for len supported properties like(string,list,tuple,dict,set)
l = ["hey", "hi", "bye", "how"]
l.sort(key=len)
print(l)

print(min(li))
print(max(li))
print(sum(li))
print(len(li))
print(li[ : : 1])
print(li[1:10])
print(li[1:10:2])
print(li)
print(li.count(10))
print(li.index(10))
li.clear()







   
a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)






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






nums = [True, False, True]
print(any(nums))
print(all(nums))