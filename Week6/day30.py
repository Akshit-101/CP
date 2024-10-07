# ------------------------------------- Rat in a Maze -------------------------------------

from typing import List

class Solution:

    # Recursive function to find all possible paths
    def solve(self, i: int, j: int, a: List[List[int]], n: int, ans: List[str], move: str, vis: List[List[int]], di: List[int], dj: List[int]):
        # Base case: if we reach the bottom-right corner, add the path to the answer
        if i == n - 1 and j == n - 1:
            ans.append(move)
            return
        
        # Defining the possible directions - Down, Left, Right, Up
        dir = "DLRU"
        
        # Looping through all 4 possible movements
        for ind in range(4):
            # Calculating the next position
            nexti = i + di[ind]
            nextj = j + dj[ind]
            
            # Checking if the next move is valid (within bounds, not visited, and path is open)
            if nexti >= 0 and nextj >= 0 and nexti < n and nextj < n and not vis[nexti][nextj] and a[nexti][nextj] == 1:
                # Marks current cell as visited
                vis[i][j] = 1
                
                # Recursive call to explore further in the chosen direction
                self.solve(nexti, nextj, a, n, ans, move + dir[ind], vis, di, dj)
                
                # Unmark the cell to backtrack
                vis[i][j] = 0

    # Function to initialize and find all paths from start to end
    def findPath(self, m: List[List[int]], n: int) -> List[str]:
        ans = []
        # Created a visited array initialized to 0
        vis = [[0 for _ in range(n)] for _ in range(n)]
        
        # Possible movements in the grid
        di = [+1, 0, 0, -1]  # Down, Left, Right, Up in terms of row index change
        dj = [0, -1, 1, 0]   # Down, Left, Right, Up in terms of column index change
        
        # If the start cell is open, begin solving
        if m[0][0] == 1:
            self.solve(0, 0, m, n, ans, "", vis, di, dj)
        
        # Return all the valid paths found
        return ans


if __name__ == "__main__":
    n = 4
    m = [[1, 0, 0, 0], [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1]]
    
    obj = Solution()
    
    # Get all possible paths from the findPath function
    result = obj.findPath(m, n)
    
    # If no path found, print -1, else print all paths
    if len(result) == 0:
        print(-1)
    else:
        for i in range(len(result)):
            print(result[i], end=" ")
    print()
