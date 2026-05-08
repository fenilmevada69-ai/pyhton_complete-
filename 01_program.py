lineno = 1
with open("txt.txt") as f:
    lines = f.readlines()    


for line in lines:
    if("python" in line):
        print(f"yes python lies in {lineno}",end="")
        break
    lineno += 1
else:
    print("python not found")