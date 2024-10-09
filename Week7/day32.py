# ----------------- Minimum Bit Flips to Convert Number --------------------
def minBitFlips(start: int, goal: int) -> int:
    # XOR of start and goal gives the differing bits
    xor = start ^ goal
    
    # Count the number of 1s in the XOR result
    return bin(xor).count('1')

start = 10
goal = 7
print(minBitFlips(start, goal)) 

# ----------------- Find the number that appears odd number of times --------------------

def singleNumber(nums):
    result = 0
    
    # XOR all the elements in the array
    for num in nums:
        result ^= num  # XOR current number with result
    
    return result  


nums1 = [2, 2, 1]
nums2 = [4, 1, 2, 1, 2]

print(singleNumber(nums1)) 
print(singleNumber(nums2)) 
 


