#strings are immutable in python
#print("Welcom " + input("Name: ") + "!")

str1 = "Apna"
str2 = "College"
finalStr = str1 + " " + str2
print(finalStr)
size = len(finalStr)
print(size)

string = "Apna College"
print(string)
# string[2] = "$" # this is invalid
print(string)

#Slicing --> topic of Machine Learning
# str(starting_idx : ending_idx(exclusive))
print(string[2:4])
print(string[3:])
print(string[:4])
print(string[-3:-1])