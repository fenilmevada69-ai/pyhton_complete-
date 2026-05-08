class Student:
    college_name = "ABC"
    name = "defaul"

    # def __init__():     # self should must present 
    #     print("Constructor is called")

    # def __init__(self):     # self should must present 
    #     print(self.name)
    #     print("Constructor is called")

    def __init__(self):     
        print("Default Constructor is called")
        pass

    def __init__(self,name,age):     # self should must present 
        print("Constructor is called")
        self.name = name
        self.age = age

    
s1 = Student("karan", 20)
print(s2.name)
print(s1.name)
print(s1.age)
print(s1.college_name)
print(Student.college_name) #valid
print(s1)
print(type(s1))