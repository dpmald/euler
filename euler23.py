# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 13:52:46 2015
@author: DanielaMaldonado

all integers greater than 28123 can be written as the sum of two abundant numbers

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
        
def abundant(n):
    divs = []    
    ans = 0
    for i in xrange(1,n):
        if n%i == 0:
            divs.append(i)
    if sum(divs) > n:
        ans = True
    else:
        ans = False
    return ans


abun = []
absums = []    
tic()
        
for i in range(12,20163):
    if abundant(i) == True:
        abun.append(i)
    i += 1

toc()

#%%

for i in abun:
    for j in abun:
        if i + j < 20161:
            if (i+j) not in absums:
                absums.append(i+j)
                
toc()

#%%

tic()

def notabsum(abun,n):
    for a in abun:
        if n - a in abun:
            return True
        return False

nabsum = 0

for i in range(1,100):
    if notabsum(abun,i):
        nabsum += i
        print i

toc()


# %%
tic()            
notabsum = []    
for i in xrange(1,20162):
    if i not in absums:
        notabsum.append(i)



toc()




