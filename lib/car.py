from vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, wheel_size, wheel_number):
        super().__init__(wheel_size, wheel_number)


    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!" 
    
    def fill_up_tank(self):
        return "filling up!"