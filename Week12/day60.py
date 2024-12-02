def numberOfSubarrays(nums, k):
    def atMost(k):
        left = 0
        count = 0
        odd_count = 0

        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                odd_count += 1

            while odd_count > k:
                if nums[left] % 2 != 0:
                    odd_count -= 1
                left += 1

            count += right - left + 1

        return count

    return atMost(k) - atMost(k - 1)
 

nums1 = [2, 4, 6]
k1 = 3
print(numberOfSubarrays(nums1, k1)) 

nums2 = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
k2 = 2
print(numberOfSubarrays(nums2, k2))  
