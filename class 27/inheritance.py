class vehicle:
    def __init__(self,name,maxspeed,mileage):
        self.name=name
        self.maxspeed=maxspeed
        self.mileage=mileage

class bus(vehicle):
    pass


b1=bus('volovo','110km/hr','12km')
print("The name of the bus ",b1.name)
print("The maxspeed of the bus ",b1.maxspeed)
print("The mileage of the bus ",b1.mileage)