from collections import defaultdict

def subarraysWithKDistinct(nums, k):
    def atMostK(nums, k):
        count = defaultdict(int)
        left = 0
        result = 0
        
        for right in range(len(nums)):
            count[nums[right]] += 1
            
            while len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    del count[nums[left]]
                left += 1
            
            result += right - left + 1
        
        return result
    
    return atMostK(nums, k) - atMostK(nums, k - 1)

# Example Usage
nums1 = [1, 2, 1, 2, 3]
k1 = 2
print(subarraysWithKDistinct(nums1, k1))  # Output: 7

nums2 = [1, 2, 1, 3, 4]
k2 = 3
print(subarraysWithKDistinct(nums2, k2))  # Output: 3
