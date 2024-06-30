#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 22:14:59 2024

@author: johannes
"""

import numpy as np
import time
import sys
sys.setrecursionlimit(3_000)

#%%

#021

t0 = time.time()

def d(n):
    total = 1
    nums = np.arange(2, n//2+1)
    array = n % nums
    for i in np.argwhere(array == 0):
        total += nums[tuple(i)]
    return total
summa = 0
for i in range(10_000):
    j = d(i)
    if i == j: pass
    elif i == d(j): summa += i
    
print(f'021: {summa}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#022

t0 = time.time()

vals = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
names = open('p022_names.txt', 'r').read().replace('"','').split(sep=',')
names.sort()
summa = 0
for i, n in enumerate(names):
    total = 0
    for j, l in enumerate(vals):
        if l in n:
            occs = n.count(l)
            total += (j+1) * occs
    summa += (i+1) * total
    
print(f'022: {summa}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#023

t0 = time.time()

abuns = []
for i in range(1, 28_123):
    if d(i) > i:
        abuns.append(i)
nums = np.asarray(abuns)
matrix = set((nums[:,None] + nums[None,:]).flatten())
total = 0
for i in range(1, 28_123):
    if i not in matrix:
        total += i
        
print(f'023: {total}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#024

t0 = time.time()
per = []

def permute(obj, j, k):
    if j == k:
        per.append(''.join(obj))
    else:
        for i in range(j, k):
            obj[j], obj[i] = obj[i], obj[j]
            permute(obj, j+1, k)
            obj[j], obj[i] = obj[i], obj[j]

digits = '0123456789'
k = len(digits)
permute(list(digits), 0, k)
sort = sorted(per)
num = sort[999_999]

print(f'024: {num}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#025

t0 = time.time()

def fib(x):
    f1, f2 = 1, 1
    for i in range(3, x, 2):
        f1 += f2
        if f1 >= x:
            return i
        f2 += f1
        if f2 >= x: 
            return i+1

print(f'025: {fib(10**999)}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#026

t0 = time.time()

def long_div(x, y):
    global l, num
    remainder = x % y
    digit = x // y
    if num > 2 * y:
        for i in range(1, len(digits) // 2):
            if digits[-i:] == digits[-2*i:-i]:
                l = i
                return
    digits.append(digit)
    num += 1
    if remainder:
        long_div(10 * remainder, y)
        
p_list = []
erato = np.arange(2, 1_000)
for i, p in enumerate(erato):
    if p: 
        erato[i+p::p] = 0
        p_list.append(p)
   
d = None
record = 1
for p in p_list:
    l = 0
    num = 1
    digits = []
    long_div(1, p)
    if l > record:
        record = l
        d = p
        
print(f'026: {d}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#027

t0 = time.time()

def quad(a, b, n):
    return n**2 + a*n + b

p_list = []
erato = np.arange(2, 10_000)
for i, p in enumerate(erato):
    if p: 
        erato[i+p::p] = 0
        p_list.append(p)

r = 1_000
record = 0
holder = None

for b in [x for x in p_list if x < r]:
    for a in range(-r, r-1):
        going = True
        for i in range(1, r):
            x = quad(a, b, i)
            if x <= 1:
                break
            elif quad(a, b, i) not in p_list:
                break
        if i > record:
            holder = a*b
            record = i
            
print(f'027: {holder}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#028

t0 = time.time()

diag = 1
summa = 1
l = 1_001
for i in range(2, l, 2):
    for j in range(4):
        diag += i
        summa += diag

print(f'028: {summa}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#029

t0 = time.time()

r1, r2 = 2, 100

a = np.arange(r1, r2+1, dtype=object)
b = np.copy(a)

powers = a[:,None]**b[None,:]
length = len(set(powers.flatten()))

print(f'029: {length}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#030

t0 = time.time()

def power(x, n):
    return np.sum(x**n)

n = 5
summa = 0
for i in range(2, (n+1) * 9**n):
    string = str(i)
    num = 0
    for d in string:
        num += int(d)**n
    if num == i:
        summa += i
        
print(f'030: {summa}')
print(f'Time (s): {time.time()-t0}\n')

sys.setrecursionlimit(1_000)