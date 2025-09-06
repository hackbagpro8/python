maths=int(input("NO. of marks obtained in maths"))
eng=int(input("NO. of marks obtained in english"))
science=int(input("NO. of marks obtained in science"))
sst=int(input("NO. of marks obtained in sst"))
total=maths+eng+science+sst

per=total/400 * 100
print("the total marks of the students are :",total)
print(f"the percentage of marks are{per}%")