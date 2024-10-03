
# ------------------------------------- N-Queens -------------------------------------
 

def solveNQueens(n):
    # This function checks if it's safe to place a queen at the current row and column
    def is_safe(row, col, diagonals, anti_diagonals, cols):
        # We check three things:
        # 1. The column is not already occupied by another queen
        # 2. The main diagonal (top-left to bottom-right) is not already occupied
        # 3. The anti-diagonal (top-right to bottom-left) is not already occupied
        if col in cols or (row - col) in diagonals or (row + col) in anti_diagonals:
            return False  # Not safe to place the queen here
        return True  # Safe to place the queen here

    # This function tries to place queens on the chessboard row by row
    def place_queens(row, diagonals, anti_diagonals, cols, current_board):
        # If we've placed queens in all rows, we've found a solution
        if row == n:
            # Add the current board configuration (which is a solution) to the result
            result.append(["".join(row) for row in current_board])
            return
        
        # Try placing a queen in each column of the current row
        for col in range(n):
            # Check if it's safe to place a queen at (row, col)
            if is_safe(row, col, diagonals, anti_diagonals, cols):
                # Place the queen on the board
                current_board[row][col] = 'Q'
                
                # Mark the column, diagonal, and anti-diagonal as occupied
                cols.add(col)  # Mark this column as having a queen
                diagonals.add(row - col)  # Mark this main diagonal as occupied
                anti_diagonals.add(row + col)  # Mark this anti-diagonal as occupied
                
                # Move to the next row and try to place the next queen
                place_queens(row + 1, diagonals, anti_diagonals, cols, current_board)
                
                # Backtrack: Remove the queen and unmark the current position
                # This is done so we can try other possibilities
                current_board[row][col] = '.'  # Remove the queen from this position
                cols.remove(col)  # Unmark this column
                diagonals.remove(row - col)  # Unmark this main diagonal
                anti_diagonals.remove(row + col)  # Unmark this anti-diagonal
    
    # This list will store all the solutions (boards) that we find
    result = []
    
    # This is our empty chessboard, filled with '.' to represent empty spaces
    current_board = [['.' for _ in range(n)] for _ in range(n)]
    
    # Start placing queens from the first row (row 0)
    place_queens(0, set(), set(), set(), current_board)
    
    # Return all the solutions (boards with queens placed correctly)
    return result

# Example usage: Solving the 4-Queens puzzle
n = 4
print(solveNQueens(n))


# This one is tough one :) 