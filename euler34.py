# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:35:00 2015

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

import math

tic()
facs = []
for i in xrange(1,10):
    facs.append(math.factorial(i))

dig = []   

def fsum(n):
    facsum = 0
    for j in range(len(str(n))):
        q = str(n)        
        if q[j] == '1':
            facsum += 1
        elif q[j] == '2':
            facsum += 2
        elif q[j] == '3':
            facsum += 6
        elif q[j] == '4':
            facsum += 24
        elif q[j] == '5':
            facsum += 120
        elif q[j] == '6':
            facsum += 720
        elif q[j] == '7':
            facsum += 5040
        elif q[j] == '8':
            facsum += 40320
        elif q[j] == '9':
            facsum += 362880
        elif q[j] == '0':
            facsum += 1
    return facsum
            
for i in range(3,2000000):
    if i == fsum(i):
        dig.append(i)
    else:
        i +=1
    
    
    
toc()
    
    