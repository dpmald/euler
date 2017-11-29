# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:39:05 2015

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
import string 

def primedig(n):
    nn = list(str(n))    
    primefam = []
    for i in range(1,len(nn)-1):
        for j in range(0,3):
            nn[i] = str(j)
            strnn = ''.join(nn)
            newnum = int(strnn)
            if isprime(newnum):
                primefam.append(newnum)
    primefam.sort()
    return primefam
x = 56993            
astring = '12345'   
z = list(astring) 
zz = ''.join(z)




