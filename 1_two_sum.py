# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:14:23 2020

@author: ffr
"""
class Solution(object):
    def twoSum(self, nums, target): 
        hash_map={}
        for index, value in enumerate(nums):
            hash_map[value]=index
        for index1,value in enumerate(nums):
            if target - value in hash_map:
                index2=hash_map[target-value]
                if index1 != index2:
                    return [index1,index2]
                

# =============================================================================
# method 2                
# =============================================================================
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]
                
# =============================================================================
# hashmap             
# =============================================================================
def two_sum(nums, target):
    hashmap = {}
    
    for index, num in enumerate(nums):
        complement = target - num
        if complement in hashmap:
            return [hashmap[complement], index]
        hashmap[num] = index
    
    return None

# Example:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)

if result:
    print(f"The indices of the two numbers that add up to the target are: {result}")
else:
    print("No two sum solution found.")