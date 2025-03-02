class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # for row in range(9):
        #     r_set = set()
        #     for col in range(9):
        #         if board[row][col] == '.':
        #             continue
        #         if board[row][col] in r_set:
        #             return False
        #         r_set.add(board[row][col])
        
        # for col in range(9):
        #     c_set = set()
        #     for row in range(9):
        #         if board[row][col] == '.':
        #             continue
        #         if board[row][col] in c_set:
        #             return False
        #         c_set.add(board[row][col])
        
        # for box_row in range(3):
        #     for box_col in range(3):
        #         b_set = set()
        #     #    for row in range(0, 9, 3):
        #     #        for col in range(0, 9, 3):
        #     #            for row in range(row, row+3):
        #     #                for col in range(col, col+3):
        #         for i in range(3):
        #             for j in range(3):
        #                 row = box_row * 3 + i
        #                 col = box_col * 3 + j
        #                 if board[row][col] == '.':
        #                     continue
        #                 if board[row][col] in b_set:
        #                     return False
        #                 b_set.add(board[row][col])
        # return True
    
    # Use a single pass through the board
    # Track seen digits with bitmasking for faster operations
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
    
        for r in range(9):
            for c in range(9):
            # Skip empty cells
                if board[r][c] == '.':
                    continue
            #convert character to integer value
                val = int(board[r][c])
#Create a bitmask for this value (e.g., 2 becomes 0b10, 5 becomes 0b10000)
                pos = 1 << (val - 1)
# Calculate box index
                box_idx = (r // 3) * 3 + c // 3
        # Check if value already exists using bitwise AND operation
                if (rows[r] & pos) or (cols[c] & pos) or (boxes[box_idx] & pos):
                    return False
 # Mark value as seen using bitwise OR operation
                rows[r] |= pos
                cols[c] |= pos
                boxes[box_idx] |= pos
    
        return True