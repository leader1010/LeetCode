# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        num = 1
        count = {}
        while p:
            count[num] = p
            p = p.next
            num += 1
        x = num - n - 1
        if x == 0:
            return head.next
        if len(count) == 1:
            return
        try:
            count[x].next = count[x + 2]
        except:
            count[x].next = None
        return head



