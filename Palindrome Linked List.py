# Given the head of a singly linked list, return true if it is a palindrome.
#
# Input: head = [1,2,2,1]
# Output: true
#
# Input: head = [1,2]
# Output: false


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = []

        while head:
            n.append(head.val)
            head = head.next

        l,r = 0, len(n)-1
        while l<=r:
            if n[l] != n[r]:
                return False
            else:
                l+=1
                r-=1
        return True