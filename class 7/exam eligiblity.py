mc= input("do you have medical cause (y/n) : ")
if mc.lower() == 'y':
    print("you are allowed to give exam")
else:
    att=int(input("enter your attendence : "))
    if att>75:
     print("you are allowed to write the exam")
    else:
       print("you are not allowed to write the exam")