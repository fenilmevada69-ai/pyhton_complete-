# inheritance ---> single, multilevel, multiple
# class Car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("Car stated...")
        
#     @staticmethod
#     def stop():
#         print("Car stopped.")
        
# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name
        
# class Fotuner(Car):
#     def __init__(self,type):
#         self.type = type
        
# car1 = ToyotaCar("Fotuner")
# car2 = ToyotaCar("prius")
# car1.start()
# car1.stop()



class Car:
    color = "black"
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car stated...")
        
    @staticmethod
    def stop():
        print("Car stopped.")
        
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
        
class Fortuner(Car):
    def __init__(self,name,typ):
        super().__init__(name)
        self.type = typ
        super().start()
        
car1 = Fortuner("Fotuner", "electric")
print(car1.type)