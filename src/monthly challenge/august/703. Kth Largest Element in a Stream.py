# accepted in 2'nd attempt

from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.priority_queue = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        current_size = len(self.priority_queue)
        peeked = None
        if current_size > 0:
            peeked = self.priority_queue[current_size-1]
        temp_stack = []
        while current_size > 0 and peeked < val:
            temp_stack.append(self.priority_queue.pop())
            current_size -= 1
            if current_size > 0:
                peeked = self.priority_queue[current_size-1]
        self.priority_queue.append(val)
        while len(temp_stack) > 0:
            self.priority_queue.append(temp_stack.pop())
        self.resize()
        current_size = len(self.priority_queue)

        return self.priority_queue[current_size-1]

    def resize(self):
        while len(self.priority_queue) > self.k:
            self.priority_queue.pop()


# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
