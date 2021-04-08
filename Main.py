from Vehicle import *
from Bus import *
from Car import *
V_Name = input("Name of Vehicle: ")
V_Fuel = input("Fuel type of vehicle: ")
C_Fuel = input("Fuel type of car: ")
C_Body = input("Body type: ")
C_Model = input("Model date: ")
B_Fuel = input("Fuel type of bus: ")
B_Type = int(input("Number of passengers: "))
V1 = Vehicle(V_Name,V_Fuel) 
C1 = Car(V_Name,C_Fuel,C_Body,C_Model)
B1 = Bus(V_Name,B_Fuel,B_Type)
V1.__str__()
C1.__str__()
B1.__str__()