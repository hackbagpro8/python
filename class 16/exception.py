try:
    n= int(input("Enter the number : "))
    print(n)
except ValueError as ex:
    print("an exception occures ",ex)