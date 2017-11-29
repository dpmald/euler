# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 09:54:58 2015

@author: DanielaMaldonado

The longest sum of consecutive primes below one-thousand that adds 
to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most 
consecutive primes?

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