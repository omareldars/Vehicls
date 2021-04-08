from Vehicle import *
class Bus(Vehicle):
    def __init__(self,name,fuel_type,number_of_passengers):
        self.name = name
        self.fuel_type = fuel_type
        self.number_of_passengers = int(number_of_passengers)
    def get_number_of_passengers(self):
        return str(self.number_of_passengers)
    def set_number_of_passengers(self, number_of_passengers):
        self.number_of_passengers = number_of_passengers
    def __str__(self):
        print("The Bus has a fuel type of bus " + self.get_fuel_type() + " with number of passengers " + self.get_number_of_passengers())