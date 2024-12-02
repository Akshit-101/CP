def characterReplacement(s, k):
    left = 0
    max_count = 0
    max_length = 0
    char_count = {}

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1
        max_count = max(max_count, char_count[s[right]])

        while (right - left + 1) - max_count > k:
            char_count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

s1 = "ABAB"
k1 = 2
print(characterReplacement(s1, k1))  # Output: 4

s2 = "AABABBA"
k2 = 1
print(characterReplacement(s2, k2))  # Output: 4
