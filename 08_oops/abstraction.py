# abstraction is one of four pillars of oops

# it is the process of hiding unnecessary implementation details while providing necessary functionality

class Car:
    def __init__(self):
        self.brake = False
        self.acc =  False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started...")

car1 = Car()

car1.start()
