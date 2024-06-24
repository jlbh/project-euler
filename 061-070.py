#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 20:53:15 2024

@author: johannes
"""

import time

t0 = time.time()
triangle = open('p067_triangle.txt', 'r').read().split()

num_rows = 100
array = [[int(triangle[0])]]
current = 1
for i in range(2, num_rows+1):
    smol = []
    for j in range(i):
        smol.append(int(triangle[current+j]))
    current += i
    array.append(smol)

for x in range(num_rows-1, 0, -1):
    for y in range(x):
        array[x-1][y] += max(array[x][y], array[x][y+1])
print(f'067: {array[0][0]}')
print(f'Time (s): {time.time()-t0}\n')