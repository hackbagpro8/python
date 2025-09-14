choice1=input("\n1.bike \n2. car\n Enter your choice(1/2): ")
if choice1=="1":
 choice2=input("\nyamaha\nscooty\n Enter your choice (1/2)")
 if choice2=="1":
   print("you have selected yamaha")
 elif choice2=="2":
   print("you have selected scooty")
 else:
   print("invalid option")
elif choice1=="2":
 choice2=input("\ncreta\nscorpio\n Enter your choice (1/2)")
 if choice2=="1":
   print("you have selected creta")
 elif choice2=="2":
   print("you have selected scorpio")
 else:
   print("invalid option")
else:
  print("invalid code")