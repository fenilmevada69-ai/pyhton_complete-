# with open("words.txt","r") as f:
#     x=f.read()
#     cnt=0
#     for i in x:
#         if i==" ":
#             cnt+=1
#     print("Total Words:",cnt+1)



# data = {"rohit":[100,20,121],"Virat":[90,98,78],"Kl":[151,89,7]}
# with open("Files/FileDict.txt",'w') as f:
#     gtotal=0
#     for i,j in data.items():
#         total=0
#         f.write(f"Player Name:{i}\n\n")
#         for i in range(0,len(j)):
#             f.write(f"Match {i+1}:{j[i]}\n")
#             total+=j[i]
        
#         f.write(f"Total:{total}\n\n")
#         gtotal+=total
#     f.write(f"Total Score:{gtotal}",)








data = {"rohit":[100,20,121],"Virat":[90,98,78],"Kl":[151,89,7]}
for i,k in data.items():
    sum=0
    with open(f"files{i}.txt",'w') as f:
        f.write(f"Player Name:{i}\n\n")
        for i in range(0,len(k)):
            
            f.write(f"Match {i+1}:{k[i]}\n")
            sum+=k[i]
            
        
        f.write(f"sum:{sum}\n\n")