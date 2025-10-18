flag=False
while not flag:
    try:
        n=int(input("enter a number : "))
        while n%2==0:
            print( "BYE BYE")
        print("no. is odd")
        flag=true
    except:
        print("invalid")
