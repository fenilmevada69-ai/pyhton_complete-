a = 10
b = 15
lcm = 0
max = 0

while True:
    if max % a == 0 and max % b == 0:
        lcm = max
        break
    max += 1
    
print(f"Lcm of {a} and {b} is {lcm}")





a = int(input("Enter a: "))
b = int(input("Enter b: "))
lcm = 0
i = 0
while(i < a*b):
    if i%a==0 and i%b==0:
        lcm = i
        break
    i += 1 
print(f"Lcm of {a} and {b} is {lcm}")