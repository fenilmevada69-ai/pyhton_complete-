import shutil
import os

if os.path.exists("Fileservice/file2.txt"):
    shutil.copy2("Filesservice/file2.txt", "filedemo2.txt")
    print("Copy of file executed")
else:
    print("File not found")
    





import shutil
# x = shutil.move("Files/user.txt","2025_Python")
# print(x)
# shutil.move("Files/usernames.txt","2025_Python")