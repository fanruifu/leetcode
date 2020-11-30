# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:17:16 2020

@author: ffr
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0 :
            a=x*-1
            b=-1*int(str(a)[::-1])
        else: 
            b=int(str(x)[::-1])
        if b<=2**31-1 and b>=-2**31:
            return(b)
        else:
            return(0)