# accepted in first attempt, arbitrary

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        ans = [None] * k

        if head is None:
            return ans

        list_size = 0
        current: ListNode = head
        while current is not None:
            list_size += 1
            current = current.next

        split_size = list_size // k
        remains = list_size % k
        current = head

        for i in range(k):
            if current is None:
                break
            
            new_list_size = split_size
            if remains > 0:
                new_list_size += 1
                remains -= 1

            new_list = current
            tail = new_list
            new_list_size -= 1

            while new_list_size > 0:
                current = current.next
                tail = tail.next
                new_list_size -= 1
            
            current = current.next
            tail.next = None
            ans[i] = new_list

        return ans
