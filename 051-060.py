#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 14:08:31 2024

@author: johannes
"""

import numpy as np
import time
import math
import sys
from fractions import Fraction

#%%

#051

t0 = time.time()

l = 6
n = 8

def get_long(x):
    for p in x:
        for i in range(10):
            numbrs = [p]
            for j in range(10):
                new = int(str(p).replace(str(i), str(j)))
                if new in x:
                    if new in numbrs or new == p: pass
                    else: numbrs.append(new)
            if len(numbrs) == n:
                return numbrs

primes = np.arange(2, 10**l)
for i, p in enumerate(primes):
    if p: primes[i+p::p] = 0
primes[:10**(l-1)] = 0
primes = primes[primes != 0]

numbers = get_long(primes)

print(f'051: {numbers[0]}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#052

t0 = time.time()

for i in range(1, 1_000_000):
    digits = sorted(str(i))
    for j in range(2, 7):
        if digits != sorted(str(i*j)):
            j=0
            break
    if j == 6:
        break

print(f'052: {i}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#053

t0 = time.time()

count=0
for n in range(23, 101):
    for k in range(1, i):
        if math.comb(n, k) > 1_000_000:
            count += 1

print(f'053: {count}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#054

t0 = time.time()

data = np.loadtxt('p054_poker.txt', dtype='U2')



print(f'054 {count}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#055

t0 = time.time()

def lychrel(x):
    for k in range(50):
        x += int(str(x)[::-1])
        string = str(x)
        if string == string[::-1]:
            return False
    return True

count = 0
for i in range(10_000):
    if lychrel(i): count += 1

print(f'055 {count}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#056

t0 = time.time()

a = np.arange(1, 100, dtype=object)
b = a[None,:]**a[:,None]
c = np.unique(b)
record = 0
for x in c:
    summa = sum([int(y) for y in list(str(x))])
    if summa > record: record = summa

print(f'056: {record}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#057

t0 = time.time()

sys.setrecursionlimit(1_100)

count = 0
def sqrt2(n):
    global count
    if n == 1: return Fraction(3 / 2)
    else:
        frac = Fraction(1 + 1 / (1 + sqrt2(n-1)))
        if len(str(frac.numerator)) > len(str(frac.denominator)):
            count += 1
        return frac

sqrt2(1_000)

print(f'057: {count}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#058

t0 = time.time()

l = 9

pcount = 0
dcount = 1 + 4*(l // 2)
k = 2
div = 4

erato = np.arange(3, l**2+1, k)
for i, p in enumerate(erato):
    if p:
        erato[i+p::p] = 0
        if (p-1) % k == 0:
            pcount += 1
            print(p)
    if (i+1) % div == 0:
        k += 2
        div *= 3

print(f'058: {pcount / dcount}')
print(f'Time (s): {time.time()-t0}\n')