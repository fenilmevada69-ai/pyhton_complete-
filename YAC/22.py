# import sys
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
# s1 = Student("karan", 20)
# x = s1
# s2 = Student("raj", 15)
# print(s1)
# print(s2.name)
# del s1
# del s2.name
# # print(s1)
# # print(s2.name)
# print("reference count: ",sys.getrefcount(x)-1)




# public private...
class Account:
    __name = "private name"
    def __init__(self, accNo, bal):
        self.__accNo = accNo
        self.bal = bal

    def getAccNo(self):
        return self.__accNo
    
    def changeAccNo(self,accNo):
        self.__accNo = accNo

c1 = Account("1234", 1000)
# print(c1.__name)  
print(c1.bal)       
c1.changeAccNo(5678)
print(c1.getAccNo())
