# try:
#     a = int(input("Enter num only: "))
# except Exception as e:
#     print(e)
# finally:
#     print("I am inside finally")
# why we use finally if finnaly will always execute
# due to function


def main():
    try:
        a = int(input("Enter num only: "))
        return
    except Exception as e:
        print(e)
        return 
    finally: 
        print("I am inside finally")
    
main()