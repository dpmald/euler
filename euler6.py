# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 10:48:39 2015

@author: DanielaMaldonado
"""
def tic():
    #Homemade version of matlab tic and toc functions
    import time
    global startTime_for_tictoc
    startTime_for_tictoc = time.time()

def toc():
    import time
    if 'startTime_for_tictoc' in globals():
        print "Elapsed time is " + str(time.time() - startTime_for_tictoc) + " seconds."
    else:
        print "Toc: start time not set"

# problem 6

natnum = range(1,101)
squares = 0
sums = 0

for i in natnum:
    squares += i*i
    sums += i

squaresum = sums*sums
print str(squaresum - squares)

tic()
# problem 10 - summation of primes
"""
this takes too long:

def isprime(a):
    if a < 2: return False
    return all(a % i for i in xrange(2, a))
    
total = 0
for i in xrange(2,1000000,1):
    if isprime(i) == True:
        total += i

print str(total)
toc()    
"""

def prime_sum(n):
    if n < 2: return 0
    if n == 2: return 2
    if n % 2 == 0: n += 1
    primes = [True] * n
    primes[0],primes[1] = [None] * 2
    sum = 0
    for ind,val in enumerate(primes):
        if val is True and ind > n ** 0.5 + 1:
            sum += ind
        elif val is True:
            primes[ind*2::ind] = [False] * (((n - 1)//ind) - 1)
            sum += ind
    return sum

tic()
print str(prime_sum(2000000))
toc()


