#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 19:14:20 2024

@author: johannes
"""

import numpy as np
import time
import math

#%%

#041

t0 = time.time()

pan = ['1','2','3','4','5','6','7']

erato = np.arange(2, 8_000_000)
for i, p in enumerate(erato):
    if p: erato[i+p::p] = 0

for p in erato[::-1]:
    if p:
        str_array = list(str(p))
        if len(str_array) == len(np.unique(str_array)):
            if '0' not in str_array:
                if sorted(str_array) == pan[:len(str_array)]:
                    break

print(f'041: {p}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#042

t0 = time.time()

vals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
words = open('p042_words.txt', 'r').read().replace('"','').split(sep=',')

def is_triangle(number):
    return (-1/2 + math.sqrt(1/4 + 2*number)).is_integer()

count = 0
for word in words:
    total = 0
    for val, letter in enumerate(vals):
        if letter in word:
            occs = word.count(letter)
            total += (val+1) * occs
    if is_triangle(total):
        count += 1

print(f'042: {count}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#043

t0 = time.time()

summa = 0
def permute(obj, j, k):
    global summa
    if j == k:
        if obj[0] != '0':
            has_prp = True
            for l, m in enumerate([2, 3, 5, 7, 11, 13, 17]):
                if int(''.join(obj[l+1:l+4])) % m != 0:
                    has_prp = False
                    break
            if has_prp:
                summa += int(''.join(obj))
    else:
        for i in range(j, k):
            obj[j], obj[i] = obj[i], obj[j]
            permute(obj, j+1, k)
            obj[j], obj[i] = obj[i], obj[j]

digits = '0123456789'
k = len(digits)
permute(list(digits), 0, k)

print(f'043: {summa}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#044

t0 = time.time()



print(f'044: {summa}')
print(f'Time (s): {time.time()-t0}\n')