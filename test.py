# max = lambda a,b : a if a>b else b
# li = [1,2,3,4,5,6,7,8,9,10]
# from functools import reduce
# print(reduce(max,li,10))




# sales = [10,20,30,40,50,60,70,80,90,100,9]
# evenoddsales = ["even" if i%2==0 else "odd" for i in sales if i>40]
# print(evenoddsales)
# evenoddsales = ["even" if i%2==0 else "odd" for i in sales if i>80]
# print(evenoddsales)






# players = [["virat", 100, 121, 89], ["rohit", 100, 67, 56]]
# sum = 0
# for score in players[0]:
#     # if type(score) == int:
#     if isinstance(score,int):
#         sum = sum + score
#     print(score)
# print(sum)



# players = [["virat", 100, 121, 89], ["rohit", 100, 67, 56]]
# for player in players:
#     sum = 0
#     for score in player:
#         if isinstance(score,int):
#             sum = sum + score
#             print(score)
#     print(f"{player[0]} score is {sum}")




# from RDS import function as f   
# print(f.div(10,2))  
# print(f.mul(10,2))  
# print(f.sum(10,2))  
# print(f.sub(10,2))  



players = [["virat", 100, 121], ["Rohit", 100, 67, 56]]
# for player in players:
#     print(player[0])


total = 0
for player in players:
    sum = 0
    for p in player:
        if(isinstance(p,int)):
            sum = sum + p
    total = total + sum
    print(f"{player[0]} score is {sum}")






data = ()
print(data)
print(type(data))
print(type(data).__name__)

# if(type(data) == tuple)
# if(type(data)__name__ =="tuple")