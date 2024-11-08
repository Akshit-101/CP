# ----------------- Next Greater Element 2 ------------------
from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nge = [-1] * n  # Initialize all elements in the result array to -1
        stack = []  # This stack will store indice s of nums in decreasing order
        
        # Loop twice to handle the circular nature
        for i in range(2 * n - 1, -1, -1):
            # Modulus allows us to wrap around the array
            while stack and nums[stack[-1]] <= nums[i % n]:
                stack.pop()  # Pop smaller elements that are not the "next greater"

            # Only assign the next greater element  if we 're in the first pass of nums
            if i < n:
                if stack:
                    nge[i] = nums[stack[-1]]  # The next greater element found
            stack.append(i % n)  # Pushing   the current index for potential next checks

        return nge


if __name__ == '__main__':
    solution = Solution()
    nums1 = [1, 2, 1]
    nums2 = [1, 2, 3, 4, 3]
    print("Example 1 Output:", solution.nextGreaterElements(nums1))  
    print("Example 2 Output:", solution.nextGreaterElements(nums2))  

# 
from typing import List

class Solution:
    def prevSmaller(self, A: List[int]) -> List[int]:
        result = []  # Result array to store nearestt smaller elements
        stack = []  # Stack to keep track ,of previous smaller elements

        for num in A:
            # Pop elements from the stack that are not     smaller than the current element
            while stack and stack[-1] >= num:
                stack.pop()
            
            # If stack is not empty, the top element   is the nearest smaller element
            if stack:
                result.append(stack[-1])
            else:
                result.append(-1)  # If . no smaller element, append -1
            
            # Pushing the current element onto the stack
            stack.append(num)

        return result


if __name__ == '__main__':
    solution = Solution()
    A1 = [4, 5, 2, 10, 8]
    A2 = [3, 2, 1]
    print("Example 1 Output:", solution.prevSmaller(A1)) 
    print("Example 2 Output:", solution.prevSmaller(A2))  
