# file writing!
f = open(r"YAC\demo.txt", "r") #(method1)by default r mode and t(text) mode other b(binary) mode
# f = open("YAC/demo.txt", "r")   #method2
# f = open("YAC\\demo.txt", "r")  #method3
allData  = f.read()
f.seek(0)
charWantData = f.read(5)
f.seek(0)
firstLineData = f.readline()

print(type(allData))
print(allData)
print(charWantData)
print(firstLineData,end="")
f.close()