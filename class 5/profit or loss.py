cp= float(input("enter the cost price of item : "))
sp=float(input("enter the selling price of item : "))

if cp<sp:
    print(f"${sp-cp} is the profit")
else:
   print(f"${cp-sp} is the loss")
