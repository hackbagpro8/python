list1=[12,34,56,67,78]
list2=[98,76,65,54,43]

print("Addition pf two list")

add_list = map(lambda x,y : x+y,list1,list2)

print(list(add_list))


def sqr(x):
    return x*x
print("the square list")
sqr_list = map(sqr,list1)
print(list(sqr_list))