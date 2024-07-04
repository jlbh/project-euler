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

penta = np.ones(2_167, dtype=np.int64)
penta[1] = 5
for i, p in enumerate(penta[:-2]):
    penta[i+2] = 2*penta[i+1] - p + 3

summa = penta[:,None] + penta[None,:]
diff = np.abs(penta[:,None] - penta[None,:])

def is_penta(number):
    return ((1 + math.sqrt(1 + 24*number)) / 6).is_integer()

record = np.inf
for index, x in np.ndenumerate(diff):
    if is_penta(x):
        if is_penta(summa[index]):
            if x < record:
                record = x

print(f'044: {record}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#045

t0 = time.time()

i, j = 40755, 41328
while True:
    i = 2*j - i + 4
    j = 2*i - j + 4
    if is_penta(i):
        k = i
        break
    elif is_penta(j):
        k = j
        break

print(f'045: {k}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#046

t0 = time.time()

primes = np.arange(2, 6_000)
for i, p in enumerate(primes):
    if p: primes[i+p::p] = 0

square = np.arange(1, 6_001)
for i, s in enumerate(square):
    if not math.sqrt(s).is_integer():
        square[i] = 0

oddcom = np.arange(2, 6_000)
oddcom -= primes
oddcom[::2] = 0

candids = primes[None,:] + 2*square[:,None]
numbers = np.unique(candids.flatten())
for odd in oddcom:
    if odd:
        if odd not in numbers:
            break

print(f'046: {odd}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#047

t0 = time.time()

primes = np.arange(2, 140_000)
for i, p in enumerate(primes):
    if p: primes[i+p::p] = 0

nums= np.arange(2, 140_000)
nums -= primes
length = 4
cons = 0

for n in nums[::-1]:
    if n:
        con = n
        count = 0
        for p in primes[:n//2+1]:
            if p:
                if n % p == 0:
                    count += 1
                    while n % p == 0:
                        n //= p
                    if n == 1 or count > length:
                        break
        if count == length:
            cons += 1
            if cons == length:
                break
        else: cons = 0
    elif cons != 0:
        cons = 0

print(f'047: {con}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#048

t0 = time.time()

def power(x):
    return x**x

summa = 0
for i in range(1, 1_000):
    summa += power(i)
string = str(summa)

print(f'048: {string[-10:]}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#049

t0 = time.time()

primes = np.arange(2, 10_000, dtype=np.int64)
for i, p in enumerate(primes):
    if p: primes[i+p::p] = 0

permlist = []
primlist = []
for p in primes[1_000:]:
    if p:
        finger = ''.join(sorted(str(p)))
        if finger not in permlist:
            permlist.append(finger)
            primlist.append([p])
        else:
            primlist[permlist.index(finger)].append(p)

findlist = []
for p in primlist:
    if len(p) >= 3:
        for pp1 in p:
            dist = []
            for pp2 in p:
                d = np.abs(pp1 - pp2)
                if d > 1_000:
                    if d not in dist:
                        dist.append(d)
                        alist = [pp1, pp2]
                    else:
                        alist.append(pp2)
                        findlist.append(alist)

final = ''.join([str (x) for x in sorted(findlist[1])])

print(f'049: {final}')
print(f'Time (s): {time.time()-t0}\n')

#%%

#050

t0 = time.time()

height = 1_000_000

primes = np.arange(2, height, dtype=np.int64)
for i, p in enumerate(primes):
    if p: primes[i+p::p] = 0

short = primes[primes != 0]
l = len(short)
record = 3
final = 0
for i in range(l):
    for j in range(record+1, l-i+1):
        summa = sum(short[i:i+j])
        if summa > height:
            break
        if j > record:
            if summa in short:
                record = j
                final = summa

print(f'050: {final}')
print(f'Time (s): {time.time()-t0}\n')
