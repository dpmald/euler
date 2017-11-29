# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:27:19 2015

@author: DanielaMaldonado

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

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
        
def isprime(n):
    if n == 2 or n == 3:
        return True
    elif n == 1:
        return False
    elif n%2 == 0:
        return False
    elif n%3 == 0:
        return False
    else:
        for i in range(2,int(n**.5)+1):            
            if n%i == 0:
                return False
        return True

def hasprime(n):
    primedivs = []    
    for i in xrange(2,n):
        if n%i == 0 and isprime(i):
            primedivs.append(i)
    return len(primedivs)
    
tic()

for i in xrange(100000,1000000):
    fourprime = []
    if hasprime(i) == 4 and hasprime(i+1) == 4 and hasprime(i+2)==4 and hasprime(i+3)==4:
        fourprime.append(i)
        break

toc()

            