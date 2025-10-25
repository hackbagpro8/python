city=input("Choose the city you have went to Los vegas/San Francisco/San diego/Seattle")

def plane_cost(city):
    if city == "Los vegas":
        return 200
    elif city == "San Francisco":
        return 180
    elif city == "San diego":
        return 250
    elif city == "Seattle":
        return 350

car=int(input("How many days have you used the rental car :"))

def rental_car_cost(car):
    if car >=7:
        return 40*car
    elif car >=3:
        return 45*car
    else:
        return 50*car


night=int(input("Enter the number of nights you would be staying"))

def hotel_cost(night):
    return night*100

total_trip_cost=hotel_cost(night)+rental_car_cost(car)+plane_cost(city)

print("The total cost of the trip would be ",total_trip_cost)
    
