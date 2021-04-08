class Vehicle(object):
    def __init__(self, name, fuel_type):
        self.name = name
        self.fuel_type = fuel_type
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_fuel_type(self):
        return self.fuel_type
    def set_fuel_type(self, fuel_type):
        self.fuel_type = fuel_type
    def __str__(self):
        print("The " + self.get_name() + " Shape has a fuel type of " + self.get_fuel_type())