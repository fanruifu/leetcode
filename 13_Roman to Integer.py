# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:11:59 2020

@author: ffr
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum_num=0
        dic={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        for i,c in enumerate(s):
            if i>0:
                if dic[s[i]]>dic[s[i-1]]:
                    sum_num=sum_num+dic[s[i]]-2*dic[s[i-1]]
                else:
                    sum_num=sum_num+dic[s[i]]
            else:
                sum_num=sum_num+dic[s[i]]
        return(sum_num)

p=Solution()
p.romanToInt('III')