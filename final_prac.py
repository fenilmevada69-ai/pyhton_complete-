dic = {
    "name" : "rahul",
    "age"  : 20,
    "topics" : ["Java", "c++" ,"C"],
    "location" : {
        "city" : "ahmedabad",
        "state" : "gujrat",
        "area" : "nikol",
    }
}


print(dic["name"])

print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.get("name"))
dic.clear()
null_dic = {}
null_dic.update({"name" : "rah", "age" : 20})
print(null_dic)