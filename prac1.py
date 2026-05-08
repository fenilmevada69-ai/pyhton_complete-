# data1 = {"ram","seeta","lakshman","kush","luv","krishna"}
# data2 = {"ram","arjunn","bhim","sahdeve","krishna","draupadi"}

# # print(data1)
# # print(data2)

# #x  = data1.union(data2)
# x = data1 | data2
# print(x)

# #x = data1.intersection(data2)
# x = data1 & data2
# print(x)

# #x = data1.difference(data2)
# x = data2 -data1
# print(x)

# x = data1.symmetric_difference(data2)
# print(x)

# y = data1.issuperset(data2)
# print(y)

# y = data2.issubset(data1)
# print(y)






# data1 = {"ram","seeta","lakshman","kush","luv","krishna"}
# data2 = {"ram","arjunn","bhim","sahdeve","krishna","draupadi"}
# print(data1)
# print(data2)
# data1.intersection_update(data2)
# #data1.symmetric_difference_update(data2)
# print(data1)



mumbai ={"raj","parth","amit","sumit"}
pune = {"jay","amit","kunal","neha"}
goa = {"rajvi","priya","amit","neha","krishna","raj"}


#find user who have attended all 3 events
x = mumbai & pune & goa
print(x)
#find user who is present in mumbai and goa
x = mumbai & goa
print(x)
#find user who is present in pune and goa
x = pune & goa
print(x)
#find user who is present in mumbai and goa but not in pune
x = (mumbai & goa) - pune
print(x)
#find user who is not present in goa but in mumbai and pune both
x = (mumbai & pune) - goa



li = [1,1,2,2,3,4,5,6,]
s = set(li)
print(s)




word = "pythonprogramming"
s = {i for i in word if i not in "aeiou"}
print(s)



names = ["Alice", "Bob", "Charlie", "David", "Alex"]
# s = set()
# for i in names:
# s.add(i[0])
# print(s)
s = set()



s = {i[0] for i in names}