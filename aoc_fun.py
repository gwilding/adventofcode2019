#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:08:43 2019

@author: georg
"""

def mode_intcode_IO(opcode,inputs=None):
    opcode_out = opcode.copy()
    if inputs != None:
        write_output= True
        outputs=[]
    else:
        write_output = False
    
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
            if inputs != None:
                opcode_out[opcode_out[k+1]] = int(inputs.pop(0))
            else:
                opcode_out[opcode_out[k+1]] = int(input())
            k += 2
        elif operation == 4: # output
            if mode[0]:
                if write_output:
                    outputs.append(opcode_out[k+1])
                else:
                    print(opcode_out[k+1])
            else:
                if write_output:
                    outputs.append(opcode_out[opcode_out[k+1]])
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
            if write_output:
                return outputs
            else:
                return opcode_out
        else:
            print("Error: Unkown operation.")
            print(k,params_opcode,operation,mode)
            return opcode_out
    if write_output:
        return outputs
    else:
        return opcode_out

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


def intcode(opcode):
    opcode_out = opcode
    k = 0
    while opcode[k] != 99:
        if opcode[k] == 1:
            opcode_out[opcode[k+3]] = opcode[opcode[k+1]] + opcode[opcode[k+2]]
        elif opcode[k] == 2:
            opcode_out[opcode[k+3]] = opcode[opcode[k+1]]*opcode[opcode[k+2]]
        elif opcode[k] == 99:
            k += 1
            return opcode_out
        k += 4
    return opcode_out