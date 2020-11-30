# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:31:28 2020

@author: ffr
"""
# =============================================================================
# works but takes too long
# =============================================================================
# class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        b=[]
        c=[]
        d=[]
        if len(s)==0:
            return(0)
        elif len(s)==1:
            return(1)
        else:
            for i in range(len(s)):
                b=[]
                for j in range(i,len(s)):
                    b.append(s[j])
                    if s[j] in b[:-1]:
                        c.append(int(len(b))-1)
                        b=[]
                    else:
                        d.append(int(len(b)))
            c.append(max(d))
            return(max(c))
    
# =============================================================================
#answer
# =============================================================================
s='qwertyqasd'
index={}
start=0
longest=0
for i,c in enumerate(s):
    if c in index and index[c]>=start:
        start=index[c]+1
    else:
        longest=max(longest,i-start+1)
    index[c]=i
print(longest)




