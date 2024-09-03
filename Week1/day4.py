# Palindrome Number problem || Approach 1: Reversing the Number
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    reversedNum = 0
    temp = x
    while temp > 0:
        digit = temp % 10
        reversedNum = reversedNum * 10 + digit
        temp //= 10
    return reversedNum == x

# || Approach 2: Two-Pointer Method
def isPalindrome(x: int) -> bool:
    s = str(x)
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


#  3Sum problem || Approach 1: Sorting and Two-Pointer Technique

def threeSum(nums):
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1  
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1  
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result


# || Approach 2: Hash Set Approach

def threeSum(nums):
    result = set()
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue 
        seen = set()
        for j in range(i + 1, len(nums)):
            complement = -nums[i] - nums[j]
            if complement in seen:
                result.add(tuple(sorted((nums[i], nums[j], complement))))
            seen.add(nums[j])
    return [list(triplet) for triplet in result]
