
# ------------------------- Subsets ------------------------------

def solve(i, nums, current, result):
    if i == len(nums):
        result.append(current[:]) 
        return
    # including the current element
    current.append(nums[i])
    solve(i + 1, nums, current, result)
    # excluding the current element
    current.pop()
    solve(i + 1, nums, current, result)

def subsets(nums):
    result = []
    solve(0, nums, [], result)
    return result

nums1 = [1, 2, 3]
print("Subsets for nums1:", subsets(nums1))

nums2 = [0]
print("Subsets for nums2:", subsets(nums2))
