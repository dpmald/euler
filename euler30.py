# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 13:48:43 2015

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


tic()
fifth = []
for i in xrange(1,100):
    fifth.append(i ** 5)

def expsum(n):
    esum = 0
    for j in range(len(str(n))):
        q = str(n)        
        if q[j] == '1':
            esum += 1**5
        elif q[j] == '2':
            esum += 2**5
        elif q[j] == '3':
            esum += 3**5
        elif q[j] == '4':
            esum += 4**5
        elif q[j] == '5':
            esum += 5**5
        elif q[j] == '6':
            esum += 6**5
        elif q[j] == '7':
            esum += 7**5
        elif q[j] == '8':
            esum += 8**5
        elif q[j] == '9':
            esum += 9**5
        elif q[j] == '0':
            esum += 0
    return esum
    
    

dig = []   

for i in xrange(2,1000000):
    if i == expsum(i):
        dig.append(i)
    

toc()