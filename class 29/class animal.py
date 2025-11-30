from abc import ABC , abstractmethod

class animal(ABC):
    @abstractmethod
    def move(self):
        pass

class Human(animal):
    def move(self):
        print("I use my legs to walk and run")


class snake(animal):
    def move(self):
        print("I move by slitherring")

class fish(animal):
    def move(self):
        print("I use my fins to move in water by swimming")
        
h1=Human()
h1.move()
s1=snake()
s1.move()
f1=fish()
f1.move()