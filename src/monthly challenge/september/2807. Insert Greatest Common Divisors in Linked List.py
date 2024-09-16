# accepted in first attempt

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        n1, n2 = head, head.next

        def gcd(a, b):
            if not b:
                return a

            return gcd(b, a % b)

        while n1 and n2:
            n1.next = ListNode(gcd(n1.val, n2.val), n2)
            n1 = n2
            n2 = n2.next

        return head
