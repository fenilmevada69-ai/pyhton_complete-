product_name = input("Enter Product Name: ")


with open("stock.txt","r") as f:
    lines = f.reallines()
    
    
    
found = False
stock = []
