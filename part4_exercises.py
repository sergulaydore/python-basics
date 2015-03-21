# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 00:50:12 2015

@author: sergulaydore
"""

"""
The basics
"""

def my_print(arg):
    print arg
    
my_print('abc')
my_print(8)
my_print([1,2,3])
my_print({'a':2, 'b':3})

# my_print('abc', 3) # gives error

"""
Arguments
"""
def adder(x, y):
    return x+y
    
print adder(2, 3)
print adder('a','b')
print adder(2.3,1.7)    

"""
varargs
"""

def adder(*args):
    if args:
        added_val = args[0]
        for val in args[1:]: added_val = added_val + val
        return added_val   
    else:
        return None
#        
print adder(2, 3)
print adder('a','b')

"""
Keywords
"""
def adder(good=1, bad=2, ugly=3):
    return good + bad + ugly

print adder(2, 3)
print adder('a','b')
kargs = {'good':3,'bad':-8}
print adder(**kargs)

def adder(**kargs):
    if kargs:
        keys = list(kargs.keys())
        added_val = kargs[keys[0]]
        for key in keys[1:]: added_val = added_val + kargs[key]
        return added_val   
    else:
        return None

adder(a=1,b=2)

"""
Dictionary tools
"""

def copyDict(old):
    new = dict() 
    for key in old.keys():
        new[key] = old[key]
    return new

d = {1:1, 2:2}
e = copyDict(d)   

"""
Dictionary tools - 2
"""

def addDict(dict1, dict2):
    new = dict()
    for key1 in dict1.keys():
        new[key1] = dict1[key1]
    for key2 in dict2.keys():
#        if key2 in new.keys():
#            new[key2].append(dict2[key2])
#        else:
        new[key2] = dict2[key2]
    return new
    
x = {1:1, 2:3}; y={2:2}
z = addDict(x, y)  
print z          

"""
More argument matching examples
"""

def f1(a, b): print a, b  # normal args
def f2(a, *b): print a, b # Positional args

def f3(a, **b): print a, b # Keyword varargs

def f4(a, *b, **c): print a, b, c # Mixed modes

def f5(a, b=2, c=3): print a, b, c # Defaults

def f6(a, b=2, *c): print a, b, c # Defaults and positional varargs

f1(1, 2)
f1(b=2, a=1)

f2(1, 2, 3)
f3(1, x=2, y=3)
f4(1, 2, 3, x=2, y=3)

f5(1)
f5(1, 4)

f6(1)
f6(1, 3, 4)

"""
Primes revisited
"""

from __future__ import division

def prime(y):
    x = y // 2
    while x>1:
        if y%x == 0: # remainder
            print y,'has factor', x
            break
        else:
            x -= 1
    else:
        print y, 'is prime'     
        
""" 
Iterations and comprehensions
"""
import math
L = [2, 4, 9, 16, 25]      

Lsqrt = []
for l in L: Lsqrt.append(math.sqrt(l)) 
print Lsqrt    

Lsqrt = map(math.sqrt, L)
print Lsqrt

Lsqrt = [math.sqrt(l) for l in L]
print Lsqrt

Lsqrt = list(math.sqrt(l) for l in L)
print Lsqrt

"""
Timing tools
"""
import timeit

timeit.timeit(stmt="import math\n[math.sqrt(x) for x in range(100)]", number=1000) # Total time
timeit.timeit(stmt="[x**.5 for x in range(100)]", number=1000) # Total time
timeit.timeit(stmt="[pow(x, .5) for x in range(100)]", number=1000) # Total time

"""
Recursive functions"""
def countdown(N):
    print N,
    if N > 0:
        countdown(N-1)
    

countdown(4)    

def countDownGen(N):
    while N>=0:
        yield N
        N -= 1
print  list(countDownGen(4))

"""       
Computing Factorials
"""

def fact0(N):
    if N > 1:
        return N * fact0(N-1)
    else:
        return 1
        
fact0(3)        

def fact1(N):
    return reduce((lambda x, y: x * y), xrange(1,N+1))

fact1(3)    

def fact2(N):
    res = 1
    for idx in range(1,N+1):
        res = res * idx
    return res   
   
fact2(3)    

def fact3(N):
    return math.factorial(N)
    
fact3(3)    

from timeit import repeat

for test in (fact0, fact1, fact2, fact3):
    print test.__name__, min(repeat(stmt=lambda: test(500), number=20, repeat=3))
    
   
        
















































    
