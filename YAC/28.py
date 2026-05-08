#list comprehension

li = [1,2,3,4,5,6,7]
newli = [i for i in li if i%2==0]
print(newli)

li = [1,2,3,4,5,6,7]
newli = [i**2 for i in li if i%2==0]
print(newli)

newli = [i for i in range(1,10)]
print(newli)

newli = [i for i in range(1,10) if i%2==0]
print(newli)