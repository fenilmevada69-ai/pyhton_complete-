theme = "light"
if(theme == "light"):
    print("color - white")
elif(theme == "dark"):
    print("color - dark")
    
    
    
age = 10
print("YEs") if age > 18 else print("No") 


age = 19
ans = ("no", "yes")[age > 18]
print(ans)


a = [1, 2]
b = a

print(a is b)   


print("YEss") if age > 18 else print("No")