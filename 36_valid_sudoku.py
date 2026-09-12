# Time complexity: O(1) - The board size is fixed (9x9), so the time complexity is constant.
# Space complexity: O(1) - The space used for the sets is also constant since the board size is fixed.

class Solution(object):
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                num = board[r][c]

                if num == ".":
                    continue

                # Box index
                box = (r // 3) * 3 + (c // 3)

                if num in rows[r] or num in cols[c] or num in boxes[box]:
                    return False
                else:
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box].add(num)
        return True