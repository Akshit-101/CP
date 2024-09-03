#  Time Complexity (TC) and Space Complexity (SC) understanding by 2Sum question

# --------------------- Approach 1: Brute Force --------------------------

def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# Time Complexity: O(n^2)
# We have a nested loop, where the outer loop runs `n` times, and for each iteration, the inner loop runs `n-1` times on average.


# Space Complexity: O(1)
# We are not using any extra space that scales with the input size, just a few variables, so the space complexity is constant.


# --------------------- Approach 2: Using a Hash Map --------------------------

def two_sum_hash_map(nums, target):
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        hash_map[num] = i

# TC: O(n)
# We traverse the list once, and for each element, we perform a constant time operation (dictionary  lookup). Hence, the time complexity is linear.

# SC: O(n)
# We store each element's index in a hash map, which in the worst case (no duplicates), will store all `n` elements.

# --------------------------- Approach 3: Sorting and Two-Pointer Technique ------------------------------

def two_sum_two_pointers(nums, target):
    nums_sorted = sorted(enumerate(nums), key=lambda x: x[1])
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums_sorted[left][1] + nums_sorted[right][1]
        if current_sum == target:
            return [nums_sorted[left][0], nums_sorted[right][0]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

# TC: O(n log n)
# Sorting the array takes O(n log n) time, and the two-pointer traversal takes O(n) time. Therefore, the overall time complexity is dominated by the sorting step.

# SC: O(n)
# We need to store the sorted array, which takes O(n) space, but no additional space is required for the two-pointer technique itself.




