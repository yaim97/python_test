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
        first_node = ListNode(0)
        pointer_node = first_node
        carry = 0 #进位

        while l1 or l2:
            new_node = ListNode(0)
            if not l1:
                sum_ = l2.val + carry
                new_node.val = sum_ % 10
                carry = sum_ // 10
                l2 = l2.next
            elif not l2:
                sum_ = l1.val + carry
                new_node.val = sum_ % 10
                carry = sum_ // 10
                l1 = l1.next
            else:
                sum_ = l1.val + l2.val + carry
                new_node.val = sum_ % 10
                carry = sum_ // 10
                l1 = l1.next
                l2 = l2.next

            pointer_node.next = new_node
            pointer_node = pointer_node.next

        if carry:
            new_node = ListNode(carry)
            pointer_node.next = new_node

        return first_node.next