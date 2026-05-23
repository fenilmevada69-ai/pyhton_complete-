# normal
x = input("Enter x: ")
print(x)
# walrus
print(x := input("Enter x: "))


#normal
n = len("hellow")
if n > 3:
    print(n)
#walrus
if(n := len("hellow")) > 3:
    print(n)


#normal
line = input()
while line != "quit":
    print(line)
    line = input()
#walrus
while (line := input()) != "quit":
    print(line)
    

if(age := 20) > 18:
    print("Eligible")
else:
    print("Not Eligible")
