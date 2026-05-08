#polymorphism

# print(1+2)                  # add
# print("Apna" + "College")   # concat
# print([1,2] + [4,5])        # merge
# dunder / magic methods



class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def showComplexNumber(self):
        print(f"{self.real} + {self.img}i")

    # def addComplex(self,num2):
    #     newReal = self.real + num2.real
    #     newImg = self.img + num2.img
    #     c = Complex(newReal, newImg)
    #     return c

    # use dunder function
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        c = Complex(newReal, newImg)
        return c
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        c = Complex(newReal, newImg)
        return c
    
        
num1 = Complex(2,3)
num1.showComplexNumber()

num2 = Complex(4,5)
num2.showComplexNumber()


num3 = num1 + num2
num3.showComplexNumber()
















# class Order:
#     def __init__(self,item,price):
#         self.item = item
#         self.price = price
#     def showPrice(self):
#         print(self.price)

#     def checkPrice(self, o2):
#         if(self.price > o2.price):
#             print(f"{self.item} is more expensive than {o2.item}")
#             return True
#         else:
#             print(f"{o2.item} is more expensive than {self.item}")
#             return False

#     def __gt__(self,o2):
#         return self.price > o2.price
        
# o1 = Order("pen",10)
# o2 = Order("pencil",20)
# print(o1>o2)