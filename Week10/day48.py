''' Trapping Rainwater
Problem Statement: Given an array of non-negative integers representation elevation of ground. 
Your task is to find the water that can be trapped after rain. '''

from typing import List




def trap(arr: List[int]) -> int:
    n = len(arr)
    prefix = [0] * n
    suffix = [0] * n
    prefix[0] = arr[0]
    for i in range(1, n):
        prefix[i] = max(prefix[i - 1], arr[i])
    suffix[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = max(suffix[i + 1], arr[i])
    waterTrapped = 0
    for i in range(n):
        waterTrapped += min(prefix[i], suffix[i]) - arr[i]
    return waterTrapped




if __name__ == "__main__":
    arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print(f"The water that can be trapped is {trap(arr)}")


# -------------------- Sum of Subarray Minimums -------------------------

from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        prev_less = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            prev_less[i] = stack[-1] if stack else -1
            stack.append(i)
        
        next_less = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            next_less[i] = stack[-1] if stack else n
            stack.append(i)
        
        result = 0
        for i in range(n):
            left_count = i - prev_less[i]
            right_count = next_less[i] - i
            result += arr[i] * left_count * right_count
            result %= MOD
        
        return result

solution = Solution()
print(solution.sumSubarrayMins([3, 1, 2, 4]))  
print(solution.sumSubarrayMins([11, 81, 94, 43, 3]))  
