# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a=''
        b=''
        while l1: #transfer Listnode l1 to list a
            a=a+str(l1.val)
            l1=l1.next
        while l2: #transfer Listnode l2 to list b
            b=b+str(l2.val)
            l2=l2.next
        r=int(a[::-1])+int(b[::-1]) # get the sum
        ll=list()
        for i in range(len(str(r))):
            ll.append(int(str(r)[len(str(r))-1-i]))
        
        dd=ListNode(int(ll[0]))
        ddd=dd
        for i in range(len(ll)-1):
            ddd.next=ListNode(int(ll[i+1]))
            ddd=ddd.next
        return(dd)