# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        node = ListNode()
        node.next=head
        temp=node 
        while (temp.next!=None):
            if temp.next.val==val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return node.next