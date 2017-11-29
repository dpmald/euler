# -*- coding: utf-8 -*-
"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.

"""

i = 0;
for a in xrange(999,100,-1):
    for b in xrange(a,100,-1):
        x = a*b
        if x > i:
            pal = str(a * b)
            #print pal
            if pal == pal[::-1]:
                i = a * b
                
