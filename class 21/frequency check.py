dic1={"coding":2,"drink":4,"buy":2,"python":2,"heloo":3}

k=2

count=0

for key,value in dic1.items():
    if value ==k:
        count+=1
        

print(f"the count of words which has {k} frequency is {count}")

