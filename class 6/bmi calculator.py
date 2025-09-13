w= float(input("enter the wieght of the person in kgs :"))
h= float(input("enter the hieght in meters"))


bmi=w/(h ** 2)

if bmi <18.5 :
    print("your bmi is",bmi)
    print("you are underwight")
elif bmi <25:
    print("your bmi is ",bmi)
    print("you are healthy") 
elif bmi <30:
    print("your bmi is ",bmi)
    print("you are Over wight")
else :
    print("your bmi is ",bmi)
    print("you are obese")
    