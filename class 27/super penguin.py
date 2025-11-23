class bird:
    def __init__(self):
        print("I am a bird")
    def wings(self):
        print("I have wings and feathers to fly")


class penguin(bird):
    def __init__(self):
        super().__init__()
        print("I am a penguin")
    def walk(self):
        print("I can walk faster")

p1 = penguin()
p1.walk()
p1.wings()