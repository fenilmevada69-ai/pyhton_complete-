# def calc(operator, *args):
#     match operator:
#         case "+":
#             sum = 0
#             for i in args:
#                 sum += i
#             print("Sum is", sum)
#         case "-":
#             diff = 
#             for i in args[::-1]:
#         case "*":
#             mul = 1
#             for i in args:
#                 mul *= i
#             print("Mul is", mul)
#         case "/":
#             div = args[0]
#             for i in args[1:]:
#                 div /= i
#             print("Div is", div)
            
            
# calc("+", 10, 20, 30)   
# calc("-", 10, 20, 30)





# def data(**kwargs):
#     print(list(kwargs.keys()))

    
# data(name="royal", age=20, salary=2000)





def checkDataOfValue(**kwargs):
    flag = True
    for i in kwargs.values():
        if type(i) != str:
            flag = False
            break
    return flag


print(checkDataOfValue(name="royal", age="20", salary="2000"))



def checkData( ** kwargs):
for i in kwargs.values():
# if type(i) != str:
#
if not isinstance(i, str:
return False
return True

return False