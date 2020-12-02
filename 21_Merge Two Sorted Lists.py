# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:01:50 2020

@author: ffr
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prev=dummy=ListNode()
        while l1 and l2:
            if l1.val > l2.val:
                prev.next=l2
                l2=l2.next
            else:
                prev.next=l1
                l1=l1.next
            prev=prev.next
        prev.next=l1 or l2
        return dummy.next