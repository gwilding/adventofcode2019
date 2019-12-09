#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:08:24 2019

@author: georg
"""

import numpy as np
import matplotlib.pyplot as plt

def get_patches(wire_path):
    move = {'R': np.array([1,0]),
        'U': np.array([0,1]),
        'L': np.array([-1,0]),
        'D': np.array([0,-1])}
    direction = {'R': 1,
        'U': 1,
        'L': -1,
        'D': -1}
    patch_list=[]
    pos=np.array([0,0])
    for pin in wire_path:
#        print(pin)
        if pin[0] in ['R','L']:
            patch_list.append( ( (pos[0], pos[0] + direction[pin[0]]*int(pin[1:])), pos[1] ) )
        elif pin[0] in ['U','D']:
            patch_list.append( ( pos[0], (pos[1], pos[1] + direction[pin[0]]*int(pin[1:])) ) )
        pos += move[pin[0]]*int(pin[1:])
    horizontal = np.array([  [k[1]] + sorted(k[0])  for k in patch_list if type(k[0]) == tuple ])
    vertical = np.array([  [k[0]] + sorted(k[1])  for k in patch_list if type(k[1]) == tuple ])
    return patch_list, horizontal, vertical

def get_crossings(patch_list_1, patch_list_2):
    horizontal_1 = np.array([  [k[1]] + sorted(k[0])  for k in patch_list_1 if type(k[0]) == tuple ])
    vertical_1 = np.array([  [k[0]] + sorted(k[1])  for k in patch_list_1 if type(k[1]) == tuple ])
    horizontal_2 = np.array([  [k[1]] + sorted(k[0])  for k in patch_list_2 if type(k[0]) == tuple ])
    vertical_2 = np.array([  [k[0]] + sorted(k[1])  for k in patch_list_2 if type(k[1]) == tuple ])
    
    crossing_list = []
    for horizontal_bridge_1 in horizontal_1:
        for possible_crossing_value in vertical_2[(horizontal_bridge_1[0] >= vertical_2[:,1]) & (horizontal_bridge_1[0] <= vertical_2[:,2]),0]:
            if (possible_crossing_value >= horizontal_bridge_1[1]) & (possible_crossing_value <= horizontal_bridge_1[2]):
                print(possible_crossing_value,horizontal_bridge_1[0])
                crossing_list.append([possible_crossing_value,horizontal_bridge_1[0]])
    for vertical_bridge_1 in vertical_1:
        for possible_crossing_value in horizontal_2[(vertical_bridge_1[0] >= horizontal_2[:,1]) & (vertical_bridge_1[0] <= horizontal_2[:,2]),0]:
            if (possible_crossing_value >= vertical_bridge_1[1]) & (possible_crossing_value <= vertical_bridge_1[2]):
                print(vertical_bridge_1[0],possible_crossing_value)
                crossing_list.append([vertical_bridge_1[0],possible_crossing_value])
    # remove trivial crossingL
    for c_i, c in enumerate(crossing_list):
        if c == [0,0]:
            crossing_list.pop(c_i)
    crossing_list = np.array(crossing_list)
    # manhatten distance
    crossings = np.c_[crossing_list,np.sum(np.abs(crossing_list),1).T]
    crossings = crossings[crossings[:,2].argsort(),:]
    return crossings


move = {'R': np.array([1,0]),
        'U': np.array([0,1]),
        'L': np.array([-1,0]),
        'D': np.array([0,-1])}
direction = {'R': 1,
        'U': 1,
        'L': -1,
        'D': -1}

load_wires = np.genfromtxt('/home/georg/georg/scripts/adventofcode2019/input_day3.txt',delimiter=',',dtype=str)

#wire_path_1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
#wire_path_2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']

wire_path_1 = list(load_wires[0])
wire_path_2 = list(load_wires[1])

patch_list_1, hor_1, vert_1 = get_patches(wire_path_1)
patch_list_2, hor_2, vert_2 = get_patches(wire_path_2)

crossings = get_crossings(patch_list_1, patch_list_2)

print("Coords:", crossings[0,:2],"M-distance:",crossings[0,2])

# plot wire paths
for l in hor_1:
    plt.hlines(*l,'r')
for l in vert_1:
    plt.vlines(*l,'r')
    
for l in hor_2:
    plt.hlines(*l,'b')
for l in vert_2:
    plt.vlines(*l,'b') 
for p in crossings:
    plt.plot(p[0],p[1],'o')


