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
    
# =============================================================================
#   recursion  
# =============================================================================
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def add_two_numbers(l1, l2, carry=0):
    if not l1 and not l2:
        if carry:
            return ListNode(carry)
        return None

    if not l1:
        l1 = ListNode(0)
    if not l2:
        l2 = ListNode(0)

    total = l1.value + l2.value + carry
    result = ListNode(total % 10)
    carry = total // 10

    result.next = add_two_numbers(l1.next, l2.next, carry)
    
    return result

# Example:
# Construct linked lists
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

# Call the function to add two numbers represented by the linked lists
result = add_two_numbers(l1, l2)

# Print the sum as a linked list
while result:
    print(result.value, end=" ")
    result = result.next