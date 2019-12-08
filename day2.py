# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 11:33:28 2019

@author: georg
"""

import numpy as np

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

path_in = 'C:/Dropbox/programming/python/adventofcode/day2_input.txt'

opcode = np.genfromtxt(path_in,delimiter=',',defaultfmt='i%i')
opcode = [int(k) for k in opcode]
opcode[1] = 12
opcode[2] = 2

opcode_out = intcode(opcode)
print(opcode_out[0])

opcode_start = np.genfromtxt(path_in,delimiter=',',defaultfmt='i%i')
opcode_start = [int(k) for k in opcode_start]
target = 19690720
for noun in range(100):
    for verb in range(100):
        opcode = opcode_start.copy()
        opcode[1] = noun
        opcode[2] = verb
        opcode_out = intcode(opcode)
#        print("noun:", noun, "verb",verb,"result:",opcode_out[0])
        if opcode_out[0] == target:
            print("noun:", noun, "verb",verb,"result:",opcode_out[0])
            print("solution:",100*noun+verb)
