# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:16:38 2020

@author: ffr
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x)==str(x)[::-1] and x<=2**31-1:
            return(True)
        else:
            return(False)
        