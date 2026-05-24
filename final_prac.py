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