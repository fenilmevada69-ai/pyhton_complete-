dict1 = {'a' : 1, 'b' : 2}
dict2 = {'c' : 3, 'd' : 4}
merged = dict1 | dict2
print(merged)



with(
    open("file1.txt", "r") as f1,
    open("file2.txt", "r") as f2
):
    print(f1.read())