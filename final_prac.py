student = {
    "name" : "fenil",
    "topic" : "programming",
    "subjects" : ["C++", "Java", "C"],    
    "marks" : (10,20,30),
    "isPass" : True,
    "course" : {
            "C++" : "royal",
            "Java" : {
                "night" : "royal",
                "day" : "red & white" 
                },
            "C" : "Tops"
        },
    "isHome" : None
}

new_dic = {
    "city" : "ahmedabad",
    "age" : 19  
}

student.update(new_dic)
print(student["city"])





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
# d1.setdefault("ss",67)    # adds key with default value (does not overwrite existing value)
# print(d1)
# """

# # task :1 
# """
# Ask user to give name and marks of 5 different students. Store them in dictionary. 

# ram 90 sita 77  ravan 66 
# output  :{"ram":90,"sita":77,"ravan":66}