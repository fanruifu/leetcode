# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:09:26 2020

@author: ffr
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        a=""
        if not strs:
            return ""
        min_length=len(min(strs,key=len))
        for j in range(min_length):
            for i in range(len(strs)-1):
                   if strs[i][j]!=strs[i+1][j]:
                        return a      
            a+=(strs[i][j])     
        return a
    
strs="pefgh","pefsa" 
p=Solution()
p.longestCommonPrefix(strs)