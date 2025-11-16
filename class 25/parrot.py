class parrot:
    species = 'maccaw'
    def __init__(self,name,age):
        self.name = name
        self.age= age


p1= parrot("jolly",2)
p2 =parrot("lilly",3)


print(f"my species is {p1.species} \n my name is {p1.name} \n my age is {p1.age}")
print(f"my species is {p2.species} \n my name is {p2.name} \n my age is {p2.age}")