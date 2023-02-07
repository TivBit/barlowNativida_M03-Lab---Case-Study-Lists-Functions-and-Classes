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

#This function was designed to store the Vehicle_type iformation.
class Vehicle_type(): 
    def __init__(self, year, make, model):
        self.year
        self.make
        self.model

#This function was designed to store the vehicle specification information.
class Vehicle_specs(Vehicle_type): 
    def __init__(self, color, engine, door, roof, *args, **kwargs):
        self.color
        self.engine
        self.door
        self.roof
             
wheels = Vehicle_specs(color="red", engine="V8", door="2-door", roof="sun-roof")
        
print(wheels)

            