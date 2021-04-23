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
        if l1==None and l2==None:
            return None
        if l1==None and l2!=None:
            return l2
        if l1!=None and l2==None:
            return l1

        new_node=ListNode()
        n=new_node
        p=l1
        q=l2
        while p!=None and q!=None:
            if p.val>=q.val:
                n.next=q
                q=q.next
                n=n.next
            else:
                n.next=p
                p=p.next
                n=n.next
        
        if p!=None:
            n.next=p
        else:
            n.next=q

        return new_node.next

        
        


