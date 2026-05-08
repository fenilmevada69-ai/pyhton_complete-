# tupples are immutable
# tup = (1,2,3,4,5,6)
# print(tup)
# print(type(tup))
# tup = ()
# print(tup)


#Exception(for single value)
# tup = (1)
# print(tup)
# print(type(tup))
# tup = (1.2)
# print(tup)
# print(type(tup))
# tup = ("Helow")
# print(tup)
# print(type(tup))
# So use , at end for single value
# tup = ("Helow",0)
# print(tup)
# print(type(tup))


tup = (1,2,3,4,5,6)
print(tup[1:3])
print(tup.index(2)) # returns index of first occurance
print(tup.count(2)) # count total occurance 
print(sorted(tup))
print(sum(tup))
print(len(tup))
print(min(tup))
print(max(tup))


#conversion of list and touple
t1 = (1,2,3,4,5)
l2 =list(t1)
l2.insert(2,"moksh")
print(tuple(l2))







tup1 = (1,2,3)
tup2 = (4,5,6)

print(tup1 + tup2)  # Concatenation
print(tup1 * 3)     # Repetition
print(2 in tup1)    # membership operator
print(4 in tup1)