# print("char:", chr(97))
# print("ord:", ord("a"))
# only works for one charcater
# print("ord:", ord("A"))
# newStr = ""
#upper
# name = input("Enter name: ")
# for i in name:
#     if(ord(i)>=97 and ord(i)<121):
#         newStr = newStr + chr(ord(i)-32)
#     else:
#         newStr = newStr + i
# print(newStr)


# name = "CSEREDvweweFFWwef"
# newStr = ""
# for i in range(len(name)):
#     ch = (name[i])
#     if(ord(ch)>=97 and ord(ch)<=121):
#         newStr += chr(ord(ch)-32)
#     else:
#         newStr += ch
# print(newStr)




# name = "java"
# ch = "z"
# count = 0
# for i in name:
#     if(i == ch):
#         print(i, "\nAscii-->", ord(i), "\nindex-->", count)
#         break
#     count += 1



# name = "javascript"
# ch = "a"
# count = 0
# occurences = 0
# for i in name:
#     if(i == ch):
#         occurences += 1
#         if(occurences == 2):
#             print(i, "\nAscii-->", ord(i), "\nindex-->", count)
#             break
#     count += 1



# data = "hi this is my code"
# space = 0
# for i in data:
#     if(i == " "):
#         space += 1
# print(f"spaces = {space}")
# print(f"words = {space+1}") #interested!



# data = "hi this is my code"
# count = 0
# for i in data:
#     if(i in "aeiou"):
#         count += 1
# print(count)



# unique_count = set()
# data = "hi this is my code"
# for i in data:
#     if(i in "aeiou"):
#         unique_count.add(i)
# count = len(unique_count)
# print(count)



# str = "hellow123"
# char = 0
# num = 0
# spchar = 0
# sum = 0
# for i in str:
#     if(i.isdigit()):
#         num += 1
#         sum += int(num)
#     elif(i in "! @#$%^&*(~`-_=+"):
#         spchar += 1
#     elif(i.isalpha()):
#         char += 1
# print(f"sum is {sum}")



print("Hello World!")
print("How are you!")