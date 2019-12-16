# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 11:40:57 2019

@author: georg

Day 16
"""

import timeit
import numpy as np
import itertools

from aoc_fun import mode_intcode, mode_intcode_IO

def main():
    """Advent of code day 16."""
    input_seq = np.array([int(k) for k in list(str(12345678))])
    with open('./input_day16.txt') as fp:
       lines = fp.readlines()
    input_seq = np.array([int(k) for k in list(lines[0].strip())]*10)
#    N = 100
##    time_start = timeit.default_timer()
##    tests()
##    time_end = timeit.default_timer()
##    print("Elapsed time for tests:", time_end - time_start)
#    print(phase_step_series2(input_seq,100)[:8])
    print(phase_step_series2(input_seq,100)[:8])
    
def tests():
    print("Run tests:")
    N = 100
    input_seq_1 = np.array([int(k) for k in list(str(80871224585914546619083218645595))]*10000)
    print(phase_step_series(input_seq_1,100)[:8])
def tests_part1():
    print("Run tests:")
    N = 100
    input_seq_1 = np.array([int(k) for k in list(str(80871224585914546619083218645595))])
#    print(phase_step_series2(input_seq_1,100)[:8])
    print(phase_step_series(input_seq_1,100)[:8])
    input_seq_2 = np.array([int(k) for k in list(str(19617804207202209144916044189917))])
#    print(phase_step_series2(input_seq_2,100)[:8])
    print(phase_step_series(input_seq_2,100)[:8])
    input_seq_3 = np.array([int(k) for k in list(str(69317163492948606335995924319873))])
#    print(phase_step_series2(input_seq_3,100)[:8])
    print(phase_step_series(input_seq_3,100)[:8])
    
    

def calculate_series_pattern(L):
    series_pattern = np.zeros(shape=(L,L))
    for k in range(L):
        series_pattern[k,:] = get_pattern(k+1,L)
    return series_pattern

def phase_step2(input_seq,all_patterns):
#    output_seq = []
    L = len(input_seq)
    output_seq = np.zeros(L)
    for k in range(L):
        output_seq[k] = np.abs(np.sum(input_seq*all_patterns[k,:]))%10
#        output_seq.append(np.abs(np.sum(input_seq*get_pattern(1+k,L)))%10)
    return output_seq

def phase_step(input_seq):
#    output_seq = []
    L = len(input_seq)
    output_seq = np.zeros(L)
    for k in range(L):
        output_seq[k] = np.abs(np.sum(input_seq*get_pattern(1+k,L)))%10
#        output_seq.append(np.abs(np.sum(input_seq*get_pattern(1+k,L)))%10)
    return output_seq

def phase_step_series2(input_seq,n):
    all_patterns = calculate_series_pattern(len(input_seq))
    next_step = phase_step2(input_seq,all_patterns)
    for k in range(n-1):
        next_step = phase_step2(next_step,all_patterns)
#        print(k)
    return "".join([str(int(k)) for k in next_step])

def phase_step_series(input_seq,n):
    next_step = phase_step(input_seq)
    for k in range(n-1):
        next_step = phase_step(next_step)
#        print(k)
    return "".join([str(int(k)) for k in next_step])
    
def get_pattern(n,L):
    return np.resize([[0]*n,[1]*n,[0]*n,[-1]*n], L+1)[1:]

def get_pattern_slow(n,L):
    base_pattern = [0, 1, 0, -1]
    multiply_pattern = [[k]*n for k in base_pattern*int(L/4+1)]
    pattern = np.array(multiply_pattern).flatten()[1:(L+1)]
    return pattern
    
if __name__ == '__main__':
    main()