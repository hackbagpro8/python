def palindrone(tuple1):
    s=0
    e= len(tuple1)-1
    while(s < e):
        if tuple1[s] != tuple1[e]:
            return False
        s+=1
        e-=1
    return True

tuple1=(1,2,3,2,1)
if palindrone(tuple1):
    print("It is a palindrone")
else:
    print("It is not a palindrone")
