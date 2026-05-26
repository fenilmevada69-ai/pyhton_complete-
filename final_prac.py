def getSum(*args):
    return sum(args)
        
        
s = getSum(1,2,3,4,5)
print(s)


def checkDt(*args):
    flag = True
    for i in args:
        if type(i) != int:
            flag = False
            break
    return flag
    
    
ans = checkDt("xys", 13,3,"ceh")
print(ans)


print("================")
def getUserData(**kwargs):
    print(kwargs.items())
    
    
getUserData(name="rahul", age=21, room=2002, xender="male")




print("=============================================================Start")


def getData(*args):
    flag = True
    for i in args:
        if not isinstance(i,str):
            flag = False
            break
    return flag

ans = getData("10",True,"raj","karana","sita","None","jim")
print(ans)
