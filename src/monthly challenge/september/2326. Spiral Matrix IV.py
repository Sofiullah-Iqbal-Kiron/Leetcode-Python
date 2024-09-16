# accepted in first attempt

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    direction_vectors = {
        "right": (+0, +1),
        "down": (+1, +0),
        "left": (+0, -1),
        "up": (-1, +0),
    }

    def get_next_direction(self, current_direction: str):
        next_direction = current_direction

        if current_direction == "right":
            next_direction = "down"
        elif current_direction == "down":
            next_direction = "left"
        elif current_direction == "left":
            next_direction = "up"
        elif current_direction == "up":
            next_direction = "right"

        return next_direction

    def get_next_pointer(self, curr_row, curr_col, curr_dir):
        row_updater, col_updater = self.direction_vectors[curr_dir]

        return curr_row + row_updater, curr_col + col_updater

    def is_valid_pointer(self, new_row, new_col, row_size, col_size, result_matrix) -> bool:
        is_valid = False

        if -1 < new_row < row_size and -1 < new_col < col_size:
            if result_matrix[new_row][new_col] == -1:
                is_valid = True

        return is_valid

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        result = [[-1 for _ in range(n)] for _ in range(m)]
        curr_row = 0
        curr_col = 0
        current_direction = "right"

        while head is not None:
            result[curr_row][curr_col] = head.val
            new_row, new_col = self.get_next_pointer(curr_row, curr_col, current_direction)
            if self.is_valid_pointer(new_row, new_col, m, n, result):
                curr_row, curr_col = new_row, new_col
            else:
                current_direction = self.get_next_direction(current_direction)
                curr_row, curr_col = self.get_next_pointer(curr_row, curr_col, current_direction)

            head = head.next

        return result
