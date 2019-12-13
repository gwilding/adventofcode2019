# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:40:03 2019

@author: georg

Day 6
"""
#from anytree import Node, RenderTree

import numpy as np

def main():
    """Advent of code day 6."""
    
    orbit_inputs = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L']
    orbit_inputs = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN']
    direct_orbit_list = []
    for orbit in orbit_inputs:
        direct_orbit_list.append(orbit.split(')'))
    
#    orbit_inputs = []
#    input_path = './input_day6.txt'
#    with open(input_path) as fp:
#       lines = fp.readlines()
#    direct_orbit_list = [line.strip().split(')') for line in lines]

    orbit_tree = {}
    fixed_orbit_list = []
    

#    print(direct_orbit_list)
    
    # search for COM
    tree_depth = 0
    tree_depth_list = [[]]
    if fixed_orbit_list == []:
        for orbit_index, orbit_pair in enumerate(direct_orbit_list):
            if 'COM' in orbit_pair:
                found_orbit = direct_orbit_list.pop(orbit_index)
                orbit_tree[found_orbit[0]] = {found_orbit[1]: {}}
                tree_depth_list[0] = [found_orbit[0]]
                tree_depth_list.append([])
                tree_depth_list[1] = [found_orbit[1]]
                tree_depth += 1
                
    
    while len(direct_orbit_list) > 0:
        for orbit_index, orbit_pair in enumerate(direct_orbit_list):
            # now travers dictionary
            search_tree_depth = 0
            not_found = True
            while not_found & (search_tree_depth <= tree_depth):
                if orbit_pair[0] in tree_depth_list[search_tree_depth]:
                    # now check all the keys at this level
                    for level_key in tree_depth_list[search_tree_depth]:
                        if orbit_pair[0] == level_key:
                            if search_tree_depth == tree_depth:
                                tree_depth_list.append([])
                                tree_depth += 1
                            found_orbit = direct_orbit_list.pop(orbit_index)
                            tree_depth_list[search_tree_depth+1].append(found_orbit[1])
                            not_found = False
                            break
                else:
                    search_tree_depth += 1
                
    orbits_at_depth = []
    for k in tree_depth_list:
        orbits_at_depth.append(len(k))
    orbits_at_depth = np.array(orbits_at_depth)
    print("Indirect orbits:",sum(np.array(range(len(orbits_at_depth)))*orbits_at_depth))
    
    orbit_tree = build_orbit_tree(orbit_inputs)
    
def build_orbit_tree(orbit_inputs):
    orbit_tree = {}
    for unformatted_orbit in orbit_inputs:
        orbit_tree[unformatted_orbit.split(')')[1]] = unformatted_orbit.split(')')[0]
    return orbit_tree

def tree_path_length(orbit_tree, orbit_list):
    parent_orbit_list = []
    for orbit in orbit_list:
        parent_orbit_list.append([])
        parent_orbit = orbit
        while parent_orbit != 'COM':
            parent_orbit = orbit_tree[parent_orbit]
            parent_orbit_list[-1].append(parent_orbit)
    min_depth = min([len(o) for o in parent_orbit_list])
    [o[::-1][:min_depth] for o in parent_orbit_list]
#    common_orbit = 
    
if __name__ == '__main__':
    main()