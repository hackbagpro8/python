def tip_waiter(amt,per):
    tip= amt*per/100
    bamt=amt+tip
    print("the total amount is $",bamt) 

amt=float(input("Enter thye AMT : "))
per=int(input("Enter the tip percentage"))

tip_waiter(amt,per)
