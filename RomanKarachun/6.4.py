class Bird:
    def __init__(self, name):
        self.name = name
    def fly(self):
        print(f"{self.name} bird can fly")
    def walk(self):
        print(f"{self.name} bird can walk")
    def __str__(self):
        return f"{self.name} can walk and fly"
        
class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        self.ration = ration
        super().__init__(name)
    def eat(self):
        print(f"It eats mostly {self.ration}")
        
class NonFlyingBird:
    def __init__(self, name, ration="fish"):
        self.name = name
        self.ration = ration
    def walk(self):
        print(f"{self.name} bird can walk")
    def eat(self):
        print(f"It eats {self.ration}")
    def swim(self):
        print(f"{self.name} bird can swim")
    def __str__(self):
        return f"{self.name} bird can walk and swim"

class SuperBird(NonFlyingBird, FlyingBird):
    def __str__(self):
        return f"{self.name} bird can walk, fly, swim and eat"
    
def main():
    b = Bird("Any")
    b.walk()
    print(str(b))
    p = NonFlyingBird("Penguin", "fish")
    p.swim()
    try:
        p.fly()
    except AttributeError as exp:
        print(exp)
    p.eat()
    c = FlyingBird("Canary")
    print(str(c))
    c.eat()
    s = SuperBird("Gull")
    print(str(s))
    s.eat()
    
if __name__ == "__main__":
    main()
