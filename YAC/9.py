#dictionarys are muttable
dic = {
    "name" : "Rahul",
    "subject" : ["physics", "chemistry", "math"],
    "topics" : ("dic", "set"),
    "key" : "value",
    "age" : 20,
    "is_adult" : True,
    22.3 : 2,
}

print(dic)
print(type(dic))
print(dic["name"])
print(dic["subject"])

dic["age"] = 21
print(dic)

null_dic = {}
# these are mutables 
# see adding new value..
null_dic["name"] = "Apna College"
print(null_dic)

#nested dic
student = {
    "name" : "rahul kumar",
    "subjects" : {
        "phy" : 97,
        "maths" : 98,
        "chem" : 95
    },
}

print(student["subjects"]["phy"])





student = {
    "name" : "rahul kumar",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95,
    }
}   

print(student.keys())
print(list(student.keys())) #type casted in lists
print(len(student))
print(len(list(student.keys())))
print(student.values())
print(list(student.values()))
print(student.items())      # see inside its in form of tuples
print(list(student.items()))
pairs = list(student.items())
print(pairs[0])     # 1st tuple
print(pairs[1])     # 2nd tuple
# both are same
print(student["name"])
print(student.get("name"))
# so difference is
# print(student["name1"])     # error
print(student.get("name1")) # no error -> none

new_dic = {"city" : "ahmbd", "age" : 16}
student.update(new_dic)
student.update({"name" : "neha kumari"})    # it will overrides
print(student)




d1={"phy" :90 , "che" :96, "math" : 98}
print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))
# print(sum(d1))
d1.clear()





# l1=["moksh","het"]
# # d2={"krishiv":90 ,"het" :90}
# """
# d2 =dict.fromkeys(l1,90)
# print(d2)
# d2["het"]=88
# print(d2)
# """
# d1={"phy" :90 , "che" :96,"com":99}

# # d1.pop("phy")  # arg : key   key delete 
# # print(d1)

# # d1.popitem()   # last key value pair 
# # print(d1)

# """
# d1.setdefault("ss",67)    #adds key with default value (does not overwrite existing value)
# print(d1)
# """

# # task :1 
# """
# Ask user to give name and marks of 5 different students. Store them in dictionary. 

# ram 90 sita 77  ravan 66 
# output  :{"ram":90,"sita":77,"ravan":66}