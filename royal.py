def checkDataType(*args):
    flag = True
    for i in args:
        if type(i) != "int":
            return flag
    return flag

checkDataType(1, 2, 3)  # True