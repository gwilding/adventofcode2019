#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:08:24 2019

@author: georg

https://www.astro.rug.nl/~bytesnbiscuits/

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
    L = 0
    for pin in wire_path:
#        print(pin)
        L += int(pin[1:])
        if pin[0] in ['R','L']:
            patch_list.append( [ (pos[0], pos[0] + direction[pin[0]]*int(pin[1:])), pos[1], L ] )
        elif pin[0] in ['U','D']:
            patch_list.append( [ pos[0], (pos[1], pos[1] + direction[pin[0]]*int(pin[1:])), L ] )
        pos += move[pin[0]]*int(pin[1:])
    horizontal = np.array([  [k[1]] + sorted(k[0])  for k in patch_list if type(k[0]) == tuple ])
    vertical = np.array([  [k[0]] + sorted(k[1])  for k in patch_list if type(k[1]) == tuple ])
    return patch_list, horizontal, vertical

def get_crossings(patch_list_1, patch_list_2):
    horizontal_1 = np.array([  [k[1]] + sorted(k[0]) + [k[2]]  for k in patch_list_1 if type(k[0]) == tuple ])
    vertical_1 = np.array([  [k[0]] + sorted(k[1]) + [k[2]]  for k in patch_list_1 if type(k[1]) == tuple ])
    horizontal_2 = np.array([  [k[1]] + sorted(k[0]) + [k[2]]  for k in patch_list_2 if type(k[0]) == tuple ])
    vertical_2 = np.array([  [k[0]] + sorted(k[1]) + [k[2]]  for k in patch_list_2 if type(k[1]) == tuple ])
    horizontal_1 = np.array([  [k[1]] + [k[0]] + [k[2]]  for k in patch_list_1 if type(k[0]) == tuple ])
    vertical_1 = np.array([  [k[0]] + [k[1]] + [k[2]]  for k in patch_list_1 if type(k[1]) == tuple ])
    horizontal_2 = np.array([  [k[1]] + [k[0]] + [k[2]]  for k in patch_list_2 if type(k[0]) == tuple ])
    vertical_2 = np.array([  [k[0]] + [k[1]] + [k[2]]  for k in patch_list_2 if type(k[1]) == tuple ])
    
    
    crossing_list = []
    for horizontal_bridge_1 in horizontal_1:
        intersecting_vertical_lines = [min(t) <= horizontal_bridge_1[0] <= max(t) for t in vertical_2[:,1] ]
        for cross_id, possible_crossing_value in enumerate(vertical_2[intersecting_vertical_lines,0]):
            intersecting_horizontal_lines = min(horizontal_bridge_1[1]) <= possible_crossing_value <= max(horizontal_bridge_1[1])
            if intersecting_horizontal_lines:
                path_length_1_horizontal = horizontal_bridge_1[2] - abs(horizontal_bridge_1[1][1] - vertical_2[intersecting_vertical_lines,0][cross_id]) 
                path_length_2_vertical = vertical_2[intersecting_vertical_lines,2][cross_id] - abs(horizontal_bridge_1[0] -vertical_2[intersecting_vertical_lines,1][cross_id][1])
#                print(possible_crossing_value,horizontal_bridge_1[0],"L:",path_length_1_horizontal,path_length_2_vertical)
                crossing_list.append([possible_crossing_value,horizontal_bridge_1[0],path_length_1_horizontal,path_length_2_vertical])
    for vertical_bridge_1 in vertical_1:
        intersecting_horizontal_lines = [min(t) <= vertical_bridge_1[0] <= max(t) for t in horizontal_2[:,1] ]
        for cross_id, possible_crossing_value in enumerate(horizontal_2[intersecting_horizontal_lines,0]):
            intersecting_vertical_lines = min(vertical_bridge_1[1]) <= possible_crossing_value <= max(vertical_bridge_1[1])
            if intersecting_vertical_lines:
                path_length_1_vertical = vertical_bridge_1[2] - abs(vertical_bridge_1[1][1] - horizontal_2[intersecting_horizontal_lines,0][cross_id]) 
                path_length_2_horizontal = horizontal_2[intersecting_horizontal_lines,2][cross_id] - abs(horizontal_2[intersecting_horizontal_lines,1][cross_id][1] - vertical_bridge_1[0])
                
#                print(vertical_bridge_1[0],possible_crossing_value,"L:",path_length_1_vertical,path_length_2_horizontal)
                crossing_list.append([vertical_bridge_1[0],possible_crossing_value,path_length_1_vertical,path_length_2_horizontal])
    # remove trivial crossingL
    for c_i, c in enumerate(crossing_list):
        if c == [0,0,0,0]:
            crossing_list.pop(c_i)
    crossing_list = np.array(crossing_list)
    # manhatten distance
    crossings = np.c_[crossing_list[:,:2],np.sum(np.abs(crossing_list[:,:2]),1).T,crossing_list[:,2:]]
    crossings = crossings[crossings[:,2].argsort(),:]
    crossings = np.c_[crossings[:,:3],np.sum(crossings[:,3:],1),crossings[:,3:]]
    return crossings


move = {'R': np.array([1,0]),
        'U': np.array([0,1]),
        'L': np.array([-1,0]),
        'D': np.array([0,-1])}
direction = {'R': 1,
        'U': 1,
        'L': -1,
        'D': -1}

try:
    load_wires = np.genfromtxt('/home/georg/georg/scripts/adventofcode2019/input_day3.txt',delimiter=',',dtype=str)
except:
    load_wires = np.genfromtxt('C:/Dropbox/programming/python/adventofcode/input_day3.txt',delimiter=',',dtype=str)

#wire_path_1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
#wire_path_2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
#
#wire_path_1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
#wire_path_2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

#wire_path_1 = ['R8','U5','L5','D3']
#wire_path_2 = ['U7','R6','D4','L4']

wire_path_1 = list(load_wires[0])
wire_path_2 = list(load_wires[1])

patch_list_1, hor_1, vert_1 = get_patches(wire_path_1)
patch_list_2, hor_2, vert_2 = get_patches(wire_path_2)

crossings = get_crossings(patch_list_1, patch_list_2)

print("Coords:", crossings[0,:2],"M-distance:",crossings[0,2])
print("Combinged length:")
print(crossings[:,:4])
print("Shortest length:",min(crossings[crossings[:,3]>0,3]))
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


