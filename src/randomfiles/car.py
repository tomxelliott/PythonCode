class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
        
    def display_car(self):
        string = "This is a " + self.color + " " + self.model + " with " + str(self.mpg) + " MPG."
        return string

    def drive_car(self):
        self.condition = "used"
        

class ElectricCar(Car):
    def __init__(self, battery_type, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg
        self.battery_type = battery_type
        
    def drive_car(self):
        self.condition = "like new"
        


my_car = ElectricCar("molten salt","Tesla","Black",800)
print my_car.condition
my_car.drive_car()
print my_car.condition
