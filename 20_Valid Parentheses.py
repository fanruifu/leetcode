# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 18:25:02 2020

@author: ffr
"""

      

# =============================================================================
# answer
# =============================================================================
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        match={'(':')','[':']','{':'}'}
        for c in s:
            if c in match:
                stack.append(c)
            else:
                if not stack or match[stack.pop()]!=c:
                    return False
        return not stack

             
p=Solution()
p.isValid(['}[]'])
# =============================================================================
# (){}[]不适用
# =============================================================================
# class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=[]
        b=[]
        m=[]
        n=[]
        e=[]
        f=[]
        x=[]
        y=[]
        z=[]
        if len(s)<=1:
            return False
        for i,c in enumerate(s):
            if c=='{':
                a.append(i)
            elif c=='}':
                b.append(i)
            elif c=='(':
                m.append(i)
            elif c==')':
                n.append(i)
            elif c=='[':
                e.append(i)
            elif c==']':
                f.append(i) 
        if len(a)!=len(b) or len(m)!=len(n) or len(e)!=len(f):
            return False
        for i in range(len(a)):
            x.append(a[i]+b[len(a)-i-1])
 
        for i in range(len(m)):
            y.append(m[i]+n[len(m)-i-1])
 
        for i in range(len(e)):
            z.append(e[i]+f[len(e)-i-1])
        l=x+y+z
        
        for i in l:
            if i!=len(s)-1:
                return False
            else:
                return True
