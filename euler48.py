# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 14:13:17 2015

@author: DanielaMaldonado

The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

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

tic()

def selfexp(n):
    return n ** n

expsum = 0
for i in xrange(1,1001):
    j = selfexp(i)
    expsum += j

expsumstr = str(expsum)    
y = len(str(expsum))
last10 = []
for i in range(y-10,y):
    last10.append(expsumstr[i])

print last10

toc()

