class Student:
    college_name = "ABC"

    @staticmethod   #decorator
    def hello():
        print("Hellow")

    def __init__(self,name,age):     # self should must present 
        print("Constructor is called")
        self.name = name
        self.age = age
    def getName(self):
        return self.name

    
s1 = Student("karan", 20)
# Student.getName(s1) in reality this prints
print(s1.getName())
print(s1.name)
print(s1.age)
Student.hello()