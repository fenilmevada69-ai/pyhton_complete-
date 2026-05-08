# with closes files automatically
# as is alias!!
with open(R"YAC\demo.txt", "r") as f:
    data = f.read()
    print(data)
    
with open(R"YAC\demo.txt", "w") as f:   # w will overwrite(truncate)
    f.write("I am string")