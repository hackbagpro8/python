amt=int(input("enter the amount to withdraw"))
note100=amt//100
note50=(amt%100)//50
note10=((amt%100)%50)//10

print("the 100 rs not",note100)
print("the 10 rs not",note10)
print("the 50 rs not",note50)