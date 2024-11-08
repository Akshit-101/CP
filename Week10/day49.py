# -----------------------  Asteroid Collision -------------------------
from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]:
                if stack[-1] < -asteroid:
                    stack.pop()
                    continue
                elif stack[-1] == -asteroid:
                    stack.pop()
                break
            else:
                stack.append(asteroid)
        return stack

solution = Solution()
print(solution.asteroidCollision([5, 10, -5]))  
print(solution.asteroidCollision([8, -8]))      
print(solution.asteroidCollision([10, 2, -5]))  



# ---------------------- Sum of Subarray Ranges -------------------------

from typing import List

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        
        for i in range(n):
            min_val, max_val = nums[i], nums[i]
            for j in range(i, n):
                min_val = min(min_val, nums[j])
                max_val = max(max_val, nums[j])
                total += max_val - min_val
                
        return total

solution = Solution()
print(solution.subArrayRanges([1, 2, 3]))     
print(solution.subArrayRanges([1, 3, 3]))      
print(solution.subArrayRanges([4, -2, -3, 4, 1]))  
