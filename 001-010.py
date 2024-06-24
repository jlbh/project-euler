#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 17:31:11 2024

@author: johannes
"""

import numpy as np
import time

#001

t0 = time.time()
total = 0
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print(f'001: {total}')
print(f'Time (s): {time.time()-t0}\n')

#002

t0 = time.time()
total = 2
fibo = [1, 2]
for fib in fibo:
    new_fibo = fib + fibo[-1]
    if new_fibo > 4_000_000:
        break
    fibo.append(new_fibo)
    if new_fibo % 2 == 0:
        total += new_fibo
print(f'002: {total}')
print(f'Time (s): {time.time()-t0}\n')

#003

t0 = time.time()
number = 600_851_475_143
for i in range(3, number//2, 2):
    if number % i == 0:
        number //= i
        if number == 1:
            break
print(f'003: {i}')
print(f'Time (s): {time.time()-t0}\n')
            
#004

t0 = time.time()
record = 1
nums = np.arange(100, 1000)
matrix = (nums[:,None] * nums[None,:] * np.tri(900, dtype=np.int64)).flatten()
for i in matrix:
    if i > record:
        string = str(i)
        if string == string[::-1]:
            record = int(string)
print(f'004: {record}')
print(f'Time (s): {time.time()-t0}\n')

#005

t0 = time.time()
total = []
for i in range(20, 2, -1):
    factors = []
    j = 1
    while i != 1:
        j += 1
        if i % j == 0:
            i //= j
            factors.append(j)
            j = 1
    total.append(factors)
    
number = 1
for x in range(20):
    record = 0
    for y in total:
        numy = y.count(x)
        if numy > record:
            record = numy
    number *= x**record
print(f'005: {number}')
print(f'Time (s): {time.time()-t0}\n')

#006

t0 = time.time()
numbers = np.arange(1, 101)
diff = numbers.sum()**2 - (numbers**2).sum()
print(f'006: {diff}')
print(f'Time (s): {time.time()-t0}\n')

#007

t0 = time.time()
number = 0
erato = np.arange(2, 200_000)
for i, p in enumerate(erato):
    if p: 
        number += 1
        erato[i+p::p] = 0
        if number == 10_001:
            break
print(f'010: {p}')
print(f'Time (s): {time.time()-t0}\n')

#008 

t0 = time.time()
number = """73167176531330624919225119674426574742355349194934
            96983520312774506326239578318016984801869478851843
            85861560789112949495459501737958331952853208805511
            12540698747158523863050715693290963295227443043557
            66896648950445244523161731856403098711121722383113
            62229893423380308135336276614282806444486645238749
            30358907296290491560440772390713810515859307960866
            70172427121883998797908792274921901699720888093776
            65727333001053367881220235421809751254540594752243
            52584907711670556013604839586446706324415722155397
            53697817977846174064955149290862569321978468622482
            83972241375657056057490261407972968652414535100474
            82166370484403199890008895243450658541227588666881
            16427171479924442928230863465674813919123162824586
            17866458359124566529476545682848912883142607690042
            24219022671055626321111109370544217506941658960408
            07198403850962455444362981230987879927244284909188
            84580156166097919133875499200524063689912560717606
            05886116467109405077541002256983155200055935729725
            71636269561882670428252483600823257530420752963450""".replace('\n', '').replace(' ', '')

length = 13
biggest = 0
for i, x in enumerate(number[:-length+1]):
    test = int(x)
    for j in range(length-1):
        test *= int(number[i+j+1])
    if test > biggest:
        biggest = test
print(f'008: {biggest}')
print(f'Time (s): {time.time()-t0}\n')

#009

t0 = time.time()
for b in range(2, 995):
    for a in range(1, b):
        c = 1000 - a - b
        if b < c: pass
        if c**2 == (a**2 + b**2):
            prod = a*b*c

print(f'009: {prod}')
print(f'Time (s): {time.time()-t0}\n')

#010

t0 = time.time()
erato = np.arange(2, 2_000_000)
for i, p in enumerate(erato):
    if p: erato[i+p::p] = 0
print(f'010: {np.sum(erato)}')
print(f'Time (s): {time.time()-t0}\n')