# data = {"ram", "krishna", "arjun"}
# data.remove("arjun") #error if elm is not present
# print(data)

# data.discard("arjuna") #if available it will remove..
# print(data)




data = {"ram","krishna","arjun"}
print(data)


data.add("bhim")
print(data)
#data.update({"seeta","bhim","arjun","lakshman"}) #iterable
#data.update(["seeta","bhim","arjun","lakshman"]) #iterable
data.update(("seeta","bhim","arjun","lakshman")) #iterable
data.update("seeta") #iterable
print(data)