li = [1,2,3,4,5]

# index = 0
# for item in li:
#     print(f"Item at index {index} is {item}")
#     index+=1
# this can be simplified using enumerate

for index,item in enumerate(li):
    print(f"Item at index {index} is {item}")
    index+=1