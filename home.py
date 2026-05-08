fruitShop = {
    "common_fruits": {
        "apple": {"price": 50, "qty": 100},
        "banana": {"price": 20, "qty": 200},
    },
    "tropical_fruits": {
        "mango": {"price": 80, "qty": 150},
        "pineapple": {"price": 100, "qty": 50},
    },
    "citrus_fruits": {
        "orange": {"price": 40, "qty": 120},
        "lemon": {"price": 10, "qty": 300},
    }
}

name = input("Enter your name: ")
print("\nWelcome to the Fruit Shop!", name)

print("\nAvailable Categories:")
for category in fruitShop:
    print(F"- {category}")

categoryChoice = input("\nSelect your category: ")

if categoryChoice in fruitShop:

    print("\nAvailable Fruits:")
    for fruit, details in fruitShop[categoryChoice].items():
        print(f"{fruit} - Price: {details['price']} Rs --> Stock: {details['qty']}")

    fruitChoice = input("\nSelect your fruit: ")

    if fruitChoice in fruitShop[categoryChoice]:

        quantity = int(input("Enter quantity: "))
        stock = fruitShop[categoryChoice][fruitChoice]["qty"]

        if quantity <= stock:
            price = fruitShop[categoryChoice][fruitChoice]["price"]
            total_price = quantity * price

            print("\n------- BILL -------")
            print("Customer:", name)
            print("Fruit:", fruitChoice)
            print("Quantity:", quantity)
            print("Total Price:", total_price, "Rs")
            print("--------------------")

        else:
            print("Not Enough Stock")

    else:
        print("Invalid fruit")

else:
    print("Invalid category")