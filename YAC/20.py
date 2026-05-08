class Student:
    college_name = "ABC"

    def __init__(self,name,age):     # self should must present 
        print("Constructor is called")
        self.name = name
        self.age = age
    def getName(self):
        return self.name

    
s1 = Student("karan", 20)
print(s1.getName())
print(s1.name)
print(s1.age)
print(s1.college_name)
print(Student.college_name) #valid
print(s1)
print(type(s1))