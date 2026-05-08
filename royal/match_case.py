match input("Enter a season (winter, spring, summer):"):
    case "winter":
        print("It is cold outside.")
    case "spring":
        print("Flowers are blooming.")
    case "summer":
        print("It's hot and sunny.")
        
        
        
choice = input("Enter your choice: ")        
match choice:
    case "Y" | "y" | "Yes" | "yes":
        print("You chose yes.")
    case "no":
        print("You chose no.")