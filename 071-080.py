#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:10:25 2024

@author: johannes
"""

import time
import math

#%%

#075

t0 = time.time()

def has_one(p):
    a = np.arange(1, p//3)
    b = np.arange(1, p//2)
    array = (p - a[None,:] - b[:,None])**2 - (a[None,:]**2 + b[:,None]**2)
    if np.count_nonzero(array == 0) == 1: return True
    else: return False

count = 0
for p in range(3, 1_500_001):
    if has_one(p): count += 1

print(f'075: {count}')
print(f'Time (s): {time.time()-t0}\n')