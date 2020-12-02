# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:15:13 2020

@author: ffr
"""
# =============================================================================
# 不满足要求“Do not allocate extra space for another array”
# =============================================================================
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=[]
        for i in nums:
            if i in r:
                r.pop()
            r.append(i)
        return(len(r))
    
p=Solution()
p.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
# =============================================================================
# answer
# =============================================================================
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        r=0
        for i in range(len(nums)):
            if i==0 or nums[i]!=nums[i-1]:
                nums[r]=nums[i]
                r+=1
        return(r)
p=Solution()
p.removeDuplicates([0,0,1,1,1,2,2,3,3,4])