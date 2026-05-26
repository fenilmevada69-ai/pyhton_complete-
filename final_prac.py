names = ["anna", "level", "radar", "madam", "civic", "noon", "racecar", "vijay", "sneha", "rohan", "alexander", "mahesh", "raj", "om", "ki"]

data = ["yes" if i==i[::-1] else "no" for i in names if len(i)>4]
data = [i for i in names if len(i)>4 and i == i[::-1]]
print(data)



data = ()
print(type(data).__name__)



words = {"hello", "by", "why", "when", "help", "solve"}
word = {i for i in words}
print(word)



x = {i[0] for i in "abcdefghijklmnopq" if i not in "abcde"}
print(x)


def data(*args):
    def processData():
        return [i**2 for i in args]
    return processData


x = data(1,2,3,4,5,6,7,8)
print(x())