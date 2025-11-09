list1=[1,2,3,4,]
list2=[100,200,300,400]

print(list(zip(list1,list2)))
print("Reverse zipping")

print(list(zip(list1,list2[::-1])))

stocks = {'reliance','infosys','tcs'}
prices={2175,1150,356}

stock_prices = {stocks:prices for stocks,prices in zip(stocks,prices)}

print(stock_prices)