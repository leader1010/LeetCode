# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k: int):

        def __rotateRight(head, k):
            if k == 0:
                return
            head.next = head.next
            __rotateRight(head, k - 1)






