list1=[23,48,90,89,90]
sum=0
for i in list1:
    sum+=i

avg=sum/len(list1)

print("the sum is ",sum)
print("the average is ",avg)
print("the smallest element is ",min(list1))
print("the biggest element is ",max(list1))    