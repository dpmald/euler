# -*- coding: utf-8 -*-
"""
collatz seq: number under 1e6 resulting in longest collatz seq

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

def collatz(n):
    seq = 1
    while n > 1:
        if n%2 == 0:
            n = n/2
        else: 
            n = 3*n + 1
        seq += 1
    return seq

def maxcol(n):
    i = 0
    p2 = 0
    count = 0 
    while i < n:        
        if collatz(i) >= p2:
            p2 = collatz(i)
            count = i            
            i += 1
        else:
            i += 1
    print count
    return p2
        
tic()
print(maxcol(2000000))
toc()