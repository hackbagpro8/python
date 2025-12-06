class op:
    def __init__(self,a):
        self.a=a
    

    def __lt__(self,other):
        if self.a < other.a:
            return f"{self.a} is less then {other.a}"
        else:
            return f"{self.a} is not less then {other.a}"

    def __eq__(self,other):
        if self.a == other.a:
            return f"{self.a} is  equal to {other.a}"

        else:
           return f"{self.a} is not equal to {other.a}"
   
obj1= op(12)
obj2=op(14)
print(obj1<obj2)
print(obj1==obj2)
