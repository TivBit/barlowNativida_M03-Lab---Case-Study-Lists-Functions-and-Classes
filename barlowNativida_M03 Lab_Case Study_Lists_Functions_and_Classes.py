# -*- coding: utf-8 -*-
"""
Created on %(Date: 06 Feb 2023)s

@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: M03 Lab - Case Study: Lists, Functions, and Classes
"""

############################################################################
#This program is designed collect input information from the user about their
#vehicle.  The program will then print out vehicle information.  

class Vehicle():
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
        
        
class Automobile(Vehicle):
    def __init__(self, car, truck, boat, plane):
        self.car = car
        self.truck = truck
        self.boat = boat
        self.plane = plane

    
    vehicle_type = int(input("What type of vehicle do you have?  1= Car, 2= Truck, =: Boat, 4= Plane: "))
    if vehicle_type == 1:
        print("You have a car.")
    elif vehicle_type == 2:
        print("You have a truck.")
    elif vehicle_type == 3:
        print("You have a boat.")
    elif vehicle_type == 4:
        print("You have a plane.")
    else:
        print("You did not enter a valid vehicle type.")


class vehicle_year(Automobile):
    def __init__(self, year):
        self.year = year
        
    year = int(input("Enter the year of your vehicle.  Ex. 2000: "))
    if year >= 1885:
        print(f"The year of your vehicle is: {year}.")
    
    else:
        print("You did not enter a valid vehicle year.")


print("Take care of your vehicle. Keep the oil changed!")