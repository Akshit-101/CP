''' Sliding Window Maximum

Problem Statement: Given an array of integers arr, there is a sliding window of size k which is moving from the very left of the array 
to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the 
max sliding window. '''

from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()
    ans = []
    for i in range(len(nums)):
        if dq and dq[0] == i - k:
            dq.popleft()

        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)
        if i >= k - 1:
            ans.append(nums[dq[0]])
    return ans

if __name__ == "__main__":
    k = 3
    arr = [4, 0, -1, 3, 5, 3, 6, 8]
    ans = maxSlidingWindow(arr, k)
    print("Maximum element in every", k, "window")
    print(" ".join(map(str, ans)))
