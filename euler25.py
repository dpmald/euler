# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 12:04:16 2015

@author: DanielaMaldonado

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""

def fibb(n):
    a,b = 1,1    
    for i in range(n-1):
        a,b = b, a+b
    return a
    
def fibblength(n):
    return len(str(fibb(n)))

















