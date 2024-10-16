# ------------------ Maximum XOR of Two Numbers in an Array ---------------------

def findMaximumXOR(nums):
    max_xor = 0
    mask = 0

    for i in range(31, -1, -1):
        mask |= (1 << i)
        prefixes = set([num & mask for num in nums])
        temp = max_xor | (1 << i)

        for prefix in prefixes:
            if temp ^ prefix in prefixes:
                max_xor = temp
                break

    return max_xor

print(findMaximumXOR([3, 10, 5, 25, 2, 8]))  # Output: 28


# ------------------ Maximum Product of Word Lengths  ---------------------

def maxProduct(words):
    n = len(words)
    bit_masks = [0] * n
    lengths = [len(word) for word in words]
    
    for i in range(n):
        for char in words[i]:
            bit_masks[i] |= (1 << (ord(char) - ord('a')))
    
    max_product = 0
    for i in range(n):
        for j in range(i + 1, n):
            if bit_masks[i] & bit_masks[j] == 0:  # No common characters
                max_product = max(max_product, lengths[i] * lengths[j])
    
    return max_product

# Example usage:
print(maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))  # Output: 16
print(maxProduct(["a","ab","abc","d","cd","bcd","abcd"]))      # Output: 4
