#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:39:06 2019

@author: wilding
"""

import numpy as np


input_data = np.genfromtxt('C:/Dropbox/programming/python/adventofcode/day1_input.txt')

def fuel_req(module_mass_array):
    return np.floor(module_mass_array/3)-2
def fuel_recursive(fuel_mass):
    if fuel_req(fuel_mass) <= 0:
        return fuel_mass
    else:
        return fuel_recursive(fuel_req(fuel_mass))

module_mass = np.sum(input_data)
#part 1 answer
module_fuel = int(np.sum(fuel_req(input_data)))

#part2:
for module_mass in input_data:
    total_fuel = module_fuel
    additional_fuel = fuel_req(total_fuel)
    while additional_fuel > 0:
        total_fuel += additional_fuel
        additional_fuel = fuel_req(additional_fuel)
        print(additional_fuel, total_fuel)
    
print(int(total_fuel))
