# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.
# https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg
#
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode(next=head)
        pre,cur = temp,head

        while cur:
            nxt = cur.next

            if cur.val == val:
                pre.next = nxt
            else:
                pre = cur
            cur = nxt

        return temp.next

