users = ["amit", "sumit", "raj", "parth"]
marks = [23,23,24,21,19]
age = [19,20,19,18,17]


for i,j,k in zip(users,marks,age):
    print(i,j,k)


for index, elm in enumerate(users):
    print(index,elm)