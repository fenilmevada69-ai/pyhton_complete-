##   @property

# #problem here
# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math
#         self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
        
#     def calPercentage(self):
#         self.percentage = str((self.phy + self.chem + self.math)/3) + "%"
        
        
# s1 = Student(90,80,70)
# print(s1.percentage)
# s1.phy = 80
# s1.calPercentage()
# print(s1.percentage)



##solution
class Student:
    def __init__(self,phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        
    @property   
    def percentage(self):
        # this method will converted in property        
        return str((self.phy + self.chem + self.math)/3) + "%"
        
s1 = Student(90,80,70)
print(s1.percentage)
s1.phy = 80
print(s1.percentage)


#there is also getter and setter decorators exists and __len__ and __str__