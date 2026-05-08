li = [1,2,3,4,5,6,7,8,9,10]
# map
square = lambda x : x*x
sqList = map(square, li)
print(sqList)
print(list(sqList))

#filter
def even(num):
    if(num%2==0): return True 
    else: return False
evenList = filter(even, li)
print(evenList)
print(list(evenList))


from functools import reduce
#sum
sum = lambda a,b : a+b
sumList = reduce(sum, li, 0)
print(sumList)
# remember: reduce need to import from functools