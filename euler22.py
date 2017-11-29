# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 11:03:38 2015

@author: DanielaMaldonado

Using names.txt ... begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to 
obtain a name score.

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
        
namefile = open("C:\Users\danielamaldonado\Documents\python\p022_names.txt","r")

names = namefile.read().replace('"', '').split(',')
names.sort()

def namescore(n):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']    
    score = 0    
    for i in n:
        score += alphabet.index(i) + 1
    return score

totsum = 0

tic()

for n in names:        
    mult = names.index(n) + 1
    totsum += mult * namescore(n)
    
print totsum
            
toc()













