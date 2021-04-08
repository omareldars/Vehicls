from datetime import date
from Vehicle import *
class Car(Vehicle):
    def __init__(self,name,fuel_type,body_type,model_date):
        self.body_type = body_type
        self.model_date = model_date
        self.name = name
        self.fuel_type = fuel_type
    def get_body_type(self):
        return self.body_type
    def set_body_type(self, body_type):
        self.body_type = body_type
    def get_model_date(self):
        return self.model_date
    def set_model_date(self, model_date):
        self.model_date = model_date
    def get_year(self):
        date = self.get_model_date().split('/')
        return date[2]
    def get_age(self):
        today = date.today()
        # dd/mm/YY
        current_date = today.strftime("%d/%m/%Y").split('/')
        value = int(current_date[2]) - int(self.get_year())
        return str(value)
    def __str__(self):
        print("The Car has a fuel type of " + self.get_fuel_type() + " with Body type: " + self.get_body_type() + " and used for " + self.get_age() + " years")