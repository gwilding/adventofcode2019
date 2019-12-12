#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 11:05:14 2019

@author: georg

day 5
"""

import numpy as np


def main():
    """Advent of code day 5."""

    opcode_load = list(np.genfromtxt('./input_day5.txt',delimiter=',',dtype=int))
#    opcode_load_2 = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,46,47,225,2,122,130,224,101,-1998,224,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1102,61,51,225,102,32,92,224,101,-800,224,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1101,61,64,225,1001,118,25,224,101,-106,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,1102,33,25,225,1102,73,67,224,101,-4891,224,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1101,14,81,225,1102,17,74,225,1102,52,67,225,1101,94,27,225,101,71,39,224,101,-132,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1002,14,38,224,101,-1786,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1,65,126,224,1001,224,-128,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1101,81,40,224,1001,224,-121,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,344,101,1,223,223,1107,677,677,224,102,2,223,223,1005,224,359,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,374,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,419,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,434,1001,223,1,223,108,226,677,224,102,2,223,223,1006,224,449,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,464,1001,223,1,223,1007,677,226,224,1002,223,2,223,1006,224,479,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,494,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,524,1001,223,1,223,7,226,226,224,102,2,223,223,1005,224,539,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,554,101,1,223,223,107,677,226,224,102,2,223,223,1006,224,569,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,584,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,614,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,629,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]
#    print(mode_intcode(opcode_test))
    mode_intcode(opcode_load)
#    tests()
    

def tests():
#    opcode_test = [1002,4,3,4,33]
#    opcode_test = [1101,100,-1,4,0]
    
    test_1 = [11103,9,8,9,10,9,4,9,99,-1,8]
    print("Equal 8: 1, not: 0")
    mode_intcode(test_1)
    print("Less than 8: 1, not: 0")
    test_2 = [11103,9,7,9,10,9,4,9,99,-1,8]
    mode_intcode(test_2)
    
    test_3 = [3,3,1108,-1,8,3,4,3,99]
    print("Equal 8: 1, not: 0")
    mode_intcode(test_3)
    test_4 = [3,3,1107,-1,8,3,4,3,99]
    print("Less than 8: 1, not: 0")
    mode_intcode(test_4)
    
    test_5 = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
    print("Input 0: 0, else 1")
    mode_intcode(test_5)
    opcode = [11103,3,1105,-1,9,1101,0,0,12,4,12,99,1]
    print("Input 0: 0, else 1")
    mode_intcode(opcode)
    
    test_7 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
              1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
              999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
    print(" 999: x <  8")
    print("1000: x == 8")
    print("1001: x >  8")
    mode_intcode(test_7)

def mode_intcode(opcode):
    opcode_out = opcode.copy()
    k = 0
#    print(k)
    value = [[], [], []]
    while opcode_out[k] != 99:
        params_opcode = str(opcode_out[k])
#        print(k,params_opcode)
        # number of instructions:
        number_of_instructions = len(params_opcode)
        # how to treat leading zeros?
        
        mode = '0'*min(5-len(params_opcode),3) + params_opcode[:-2]
        operation = int(params_opcode[-2:])
        # separate into single modes:
        mode = [int(m) for m in mode[::-1]]
        # get values from immediate/position
        # 0/False is position mode
        # 1/True is immediate mode
        # treat the first 2 as reading variables from the opcode
        # 3, output/writing variables to opcode comes later
        value = [[], [], []]
        if operation in [1,2,5,6]:
            for value_index, m in enumerate(mode[:2]):
    #            print(m,value_index,value)
                if m:
    #                print("immediate")
                    value[value_index] = opcode_out[k + 1 + value_index]
                else:
                    value[value_index] = opcode_out[opcode_out[k + 1 + value_index]]
        # equal or less than operation needs all three parameters
        if operation in [7,8]:
            for value_index, m in enumerate(mode):
    #            print(m,value_index,value)
                if m:
    #                print("immediate")
                    value[value_index] = opcode_out[k + 1 + value_index]
                else:
                    value[value_index] = opcode_out[opcode_out[k + 1 + value_index]]
        

        if operation == 1: # addition, writing to [position of] parameter 3 (index 2)
            if mode[2]:
                opcode_out[k+3] = value[0] + value[1]
            else:
                opcode_out[opcode_out[k+3]] = value[0] + value[1]
            k += 4
        elif operation == 2: # mutiplication, writing to [position of] parameter 3 (index 2)
            if mode[2]:
                opcode_out[k+3] = value[0]*value[1]
            else:
                opcode_out[opcode_out[k+3]] = value[0]*value[1]
            k += 4
        elif operation == 3: # input, always write to position, never immediate
            opcode_out[opcode_out[k+1]] = int(input())
            k += 2
        elif operation == 4: # output
            if mode[0]:
                print(opcode_out[k+1])
            else:
                print(opcode_out[opcode_out[k+1]])
            k += 2
        elif operation == 5: # pointer jump: 1 operation, 2 parameters
            if value[0] != 0:
                k = value[1]
            else:
                k += 3
        elif operation == 6:
            if value[0] == 0:
                k = value[1]
            else:
                k += 3
        elif operation == 7:
            if value[0] < value[1]:
                if mode[2]:
                    opcode_out[k+3] = 1
                else:
                    opcode_out[opcode_out[k+3]] = 1
            else:
                if mode[2]:
                    opcode_out[k+3] = 0
                else:
                    opcode_out[opcode_out[k+3]] = 0
            k += 4
        elif operation == 8:
            if value[0] == value[1]:
                if mode[2]:
                    opcode_out[k+3] = 1
                else:
                    opcode_out[opcode_out[k+3]] = 1
            else:
                if mode[2]:
                    opcode_out[k+3] = 0
                else:
                    opcode_out[opcode_out[k+3]] = 0
            k += 4
        elif operation == 99:
            k += 1
            return opcode_out
        else:
            print("Error: Unkown operation.")
            print(k,params_opcode,operation,mode)
            return opcode_out
    return opcode_out
        
#        if opcode[k] == 1:
#            opcode_out[opcode[k+3]] = opcode[opcode[k+1]] + opcode[opcode[k+2]]
#        elif opcode[k] == 2:
#            opcode_out[opcode[k+3]] = opcode[opcode[k+1]]*opcode[opcode[k+2]]
#        elif opcode[k] == 3:
#            opcode_out[opcode[k+1]] = input_value
#        elif opcode[k] == 4:
#            print(opcode_out[opcode[k+1]])
#        elif opcode[k] == 99:
#            k += 1
#            return opcode_out
#        k += 4
    



if __name__ == '__main__':
    main()
