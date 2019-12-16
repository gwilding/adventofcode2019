# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:50:09 2019

@author: georg

Day 7.
"""


import numpy as np
import itertools

from aoc_fun import mode_intcode, mode_intcode_IO

def main():
    """Advent of code day 7."""
    program_day7 = list(np.genfromtxt('./input_day7.txt',delimiter=',',dtype=int))
    current_highest = -np.inf
    for i in itertools.permutations([0, 1, 2, 3, 4]):
        current_highest = max(current_highest,get_phase_setting_result(program_day7,list(i)))
    print(current_highest)
    
    
    program_4 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    out = [0]
    mode_intcode_IO(program_4,inputs=[0,9])
    mode_intcode(program_4)
    9,8,7,6,5
    
def tests():
    program_1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    phase_sequence = [4,3,2,1,0]
    out = [0]
    for phase_setting in phase_sequence:
        out = mode_intcode_IO(program_1,inputs=[phase_setting,out[0]])
    print(out[0])
    program_2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
    current_highest = -np.inf
    for i in itertools.permutations([0, 1, 2, 3, 4]):
        current_highest = max(current_highest,get_phase_setting_result(program_2,list(i)))
    print(current_highest)
    
    program_3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    current_highest = -np.inf
    for i in itertools.permutations([0, 1, 2, 3, 4]):
        current_highest = max(current_highest,get_phase_setting_result(program_3,list(i)))
    print(current_highest)
    
    # 
    
    
    
def get_phase_setting_result(program, phase_sequence):
    out = [0]
    for phase_setting in phase_sequence:
        out = mode_intcode_IO(program,inputs=[phase_setting,out[0]])
    return out[0]

    
if __name__ == '__main__':
    main()