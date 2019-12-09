#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:08:43 2019

@author: georg
"""

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