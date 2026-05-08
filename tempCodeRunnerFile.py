def users(*args):
    print(args)

users("ram", "shyam", ["ok"])
users()
users("ram", "shyam", ("ok",))

def students(x,*names):
    print(names)
    print(x)

students("hiu", "how", "are", "you", 1)