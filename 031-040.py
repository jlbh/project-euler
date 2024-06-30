#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 14:22:25 2024

@author: johannes
"""

import numpy as np
import time
import math
import sys

#%%

#031

sys.setrecursionlimit(10_000_000)

t0 = time.time()

coin = np.array([1, 2, 5, 10, 20, 50, 100, 200])
comb = np.zeros(len(coin), dtype=np.int16)
total = 200
number = 0

def search(x, k):
    global number
    if k == -1:
        return
    summa = x @ coin
    while summa < total:
        search(x, k-1)
        x[k] += 1
        summa += coin[k]
    if summa == total:
        number += 1
    if k == 7:
        print(f'031: {number}')
        print(f'Time (s): {time.time()-t0}\n')
        sys.exit(0)
    x[k+1] += 1
    x[:k+1] = 0
    search(x, k+1)

search(comb, 0)

#%%

sys.setrecursionlimit(1_000)

#%%

#032

t0 = time.time()

numbers = [str(i) for i in range(1, 10)]
products = []

for a in range(2, 51):
    aa = list(str(a))
    for b in range(100, 2000):
        bb = list(str(b))
        c = a * b
        cc = list(str(c))
        if numbers == sorted(aa + bb + cc):
            products.append(c)

summa = np.sum(np.unique(products))

print(f'032: {summa}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#033

t0 = time.time()

lista = []

def options(i, j, k, l):
    if l > 1: d = (10*i + k)
    else: d = (10*k + i)
    if l % 2 == 0: n = (10*i + j)
    else: n = (10*j + i)
    return n, d

for i in range(1,10):
    for j in range(1,10):
        for k in range(2,10):
            if j == k or j / k > 1:
                pass
            else:
                for l in range(4):
                    if j / k > 1:
                        pass
                    n, d = options(i, j, k, l)
                    if n == 0 or d == 0:
                        pass
                    if n * k == d * j:
                        lista.append([j, k])

summa = np.prod(lista, axis=0)

for i in range(min(summa), 2, -1):
    if summa[0] % i == summa[1] % i == 0:
        summa //= i

print(f'033: {summa[1]}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#034

t0 = time.time()

factorials = [math.factorial(x) for x in range(10)]

sum1 = 0
def test(x):
    global sum1
    digits = sorted(list(str(x)))[::-1]
    sum2 = 0
    for d in digits:
        sum2 += factorials[int(d)]
        if x < sum2:
            return
    if x == sum2:
        sum1 += x

for x in range(10, 10_000_000):
    test(x)

print(f'034: {sum1}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#035

t0 = time.time()

circ = 0

erato = np.arange(2, 1_000_000)
for i, p in enumerate(erato):
    if p: erato[i+p::p] = 0

for e in erato:
    if e != 0:
        digits = list(str(e))
        circular = True
        for i in range(1, len(digits)):
            new = int(''.join(np.roll(digits, i).tolist()))
            if erato[new-2] == 0:
                circular = False
                break
        if circular:
            circ += 1

print(f'035: {circ}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#036

t0 = time.time()

def binary(x):
    y = ''
    for i in range(20, -1, -1):
        j = 2**i
        if x >= j:
            x -= j
            y += '1'
        elif len(y) != 0:
            y += '0'
    return y

def palin(x):
    for j in range(len(x) // 2):
        if x[j] != x[-j-1]:
            return False
    return True

summa = 0
for i in range(1_000_000):
    string = str(i)
    if palin(string):
        string = binary(i)
        if palin(string):
            summa += i

print(f'036: {summa}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#037

t0 = time.time()

erato = np.arange(2, 1_000_000)
for i, p in enumerate(erato):
    if p: erato[i+p::p] = 0

digits = [str(x) for x in range(1, 10)]
numbers1 = []
numbers2 = []

def extend(x):
    for d in digits:
        new = x + d
        if int(new) > 1_000_000:
            return
        if erato[int(new) - 2] != 0:
            numbers1.append(new)
            extend(new)

def reduce(x):
    if erato[int(x[-1]) - 2] == 0:
        return
    for i in range(1, len(x)-1):
        if erato[int(x[i:]) - 2] == 0:
            return
    numbers2.append(x)

for d in ['2', '3', '5', '7']:
    extend(d)
for n in numbers1:
    reduce(n)

nums = np.unique(numbers2).tolist()
summa = sum([int(x) for x in nums])

print(f'037: {summa}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#038

t0 = time.time()

record = 0

for i in range(10_000):
    string = str(i)
    if len(string) == len(np.unique(list(string))):
        for j in range(2, 100):
            new = str(i * j)
            if '0' not in list(new):
                string += new
            else: break
            if len(string) >= 9:
                break
        if len(string) == len(np.unique(list(string))) == 9:
            if int(string) > record:
                record = int(string)

print(f'038: {record}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#039

t0 = time.time()

most = 0
record = None
for p in range(3, 1_001):
    num = 0
    for a in range(1, p // 3):
        for b in range(a, p // 2):
            if a + b + math.sqrt(a**2 + b**2) == p:
                num += 1
    if num > most:
        most = num
        record = p

print(f'038: {record}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#040

t0 = time.time()

i = 1
k = 1
n = 1
prod = 1
while n < 1_000_042:
    l = len(str(i))
    d = k - n
    if l > d:
        prod *= int(str(i)[d])
        k *= 10
    i += 1
    n += l

print(f'040: {prod}')
print(f'Time (s): {time.time()-t0}\n')