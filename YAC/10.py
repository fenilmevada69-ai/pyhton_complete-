# same as 11th sets
# sets are unordered and having unique and immutable values
# means it can stores(hashable values) int, float, string, tuple... cant store list dic...
# it print in any ordered 
collection = {1,2,4,2,"hellow!","world", "world"}
print(collection)
print(type(collection))
print(len(collection))


# how to print empty set
empty_set = {}    # this is acutully empty dictionary
print(type(empty_set))
em_set = set()    # method to create empty set
print(type(em_set))
print((em_set))

# sets are mutable 
# but sets elements are immutable
em_set.add(10);    
em_set.add(20);   
em_set.add(30);   
em_set.add(40);   
em_set.remove(10);  #error if item not found
em_set.discard(10)  #no error if item not found
# em_set.remove(7);   # key-error
em_set.add("string");   # adding string
em_set.add((1,2,3));   # adding tuple
# em_set.add([1,2,3]);   # adding list 
# em_set.add({"name" : "rahul", "age" : 290});   # adding dictionary 
# will give unhashable type error
# set contains only hashable values
print(em_set)
print(len(em_set))
em_set.clear()
print(len(em_set))
#unhashable ---> list, dic, sets  (as this 3 ares mutable)
#immutbale ---> has some hashvalue






# set.pop()  it removes random value from set
collection = {"hello", "apnaCollege", "world", "coding", "python"}
print(collection.pop())
print(collection.pop())
print(collection.pop())



# union and intersection and returns new set (same as 11th maths)
set1 = {1,2,3}
set2 = {3,4,5}
setu = set1.union(set2)
print(setu)
seti = set1.intersection(set2)
print(seti)





set1 = {1,2,3}
set2 = {3,4,5}
set1.update(set2)
# update --> set1 |= set2
# union --> set1 | set2
print(set1)
print(set2)
# OR setu = set1.union(set2)
set1 = {1,2,3}
set2 = {3,4,5,6,2,1}
set1.add(6)
print(set1)
print(set2)
print(set1.difference(set2))    # 1 mese 2 ka nikal diya
print(set1.issubset(set2))
print(set1.issuperset(set2))








data1 = {"ram","seeta","lakshman","kush","luv","krishna"}
data2 = {"ram","arjunn","bhim","sahdeve","krishna","draupadi"}

# print(data1)
# print(data2)

#x  = data1.union(data2)
x = data1 | data2
print(x)

#x = data1.intersection(data2)
x = data1 & data2
print(x)

#x = data1.difference(data2)
x = data2 -data1
print(x)

x = data1.symmetric_difference(data2)
print(x)

y = data1.issuperset(data2)
print(y)

y = data2.issubset(data1)
print(y)

data1 = {"ram","seeta","lakshman","kush","luv","krishna"}
data2 = {"ram","arjunn","bhim","sahdeve","krishna","draupadi"}
print(data1)
print(data2)
data1.intersection_update(data2)
#data1.symmetric_difference_update(data2)


print(data1)