##class method
# class Person:
#     name = "anonymous"
    
#     def changeName(self, name):
#         # Person.name = name            #method 1
#         self.__class__.name = name      #method 2
        
# p1 = Person()
# p1.changeName("rahul kumar")
# print(p1.name)
# print(Person.name)





#proper method
class Person:
    name = "anonymous"
    
    @classmethod
    def changeName(cls,name):
        cls.name = name      #method 2
        
p1 = Person()
print(p1.name)
print(Person.name)
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)



"""3 methods in python
        
    static method
    class method(cls)        
    instance method(self)
        
"""