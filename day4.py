# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 23:02:16 2019

@author: georg

day 4
"""

lower = 231832
higher = 767346
puzzle_inputs = range(lower,higher+1)
count = 0
for i in puzzle_inputs:
    # 6 digit number
    lenght_rule = len(str(i)) == 6
    range_rule = lower <= i <= higher
    same_rule = any([str(i)[k] == str(i)[k+1] for k in range(len(str(i))-1)])
    increase_rule = all(np.diff(np.array([int(k) for k in str(i)])) >= 0)
    difference = np.diff(np.array([int(k) for k in str(i)])) == 0
    double_rule = []
    for ind, d in enumerate(difference):
        if d:
            double_rule.append(np.sum(difference[max(ind-1,0):min(ind+2,len(difference))]) )
    double_rule = 1 in double_rule
#    double_rule = any([difference[k:k+3] for k in range(len(difference)-2) if difference[k+1] ])
#    double_rule = any([np.sum([difference[k:k+3]]) == 1 for k in range(len(difference)-2) if difference[k+1] ])
    if lenght_rule & range_rule & same_rule & increase_rule & double_rule:
        count += 1
        
print(count)