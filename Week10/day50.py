# ---------------------- Maximal Rectangle -------------------------

from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:
            for col in range(cols):
                if row[col] == '1':
                    heights[col] += 1
                else:
                    heights[col] = 0
            
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        heights.pop()
        return max_area

solution = Solution()
print(solution.maximalRectangle([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))  
print(solution.maximalRectangle([["0"]])) 
print(solution.maximalRectangle([["1"]])) 
