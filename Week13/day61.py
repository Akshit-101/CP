def lengthOfLongestSubstringKDistinct(s: str, k: int) -> int:
    if k == 0 or not s:
        return 0

    left = 0
    char_count = {}
    max_length = 0

    for right in range(len(s)):
        char = s[right]
        char_count[char] = char_count.get(char, 0) + 1

        # Shrink the window until we have at most k distinct characters
        while len(char_count) > k:
            left_char = s[left]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            left += 1

        # to Calculate max length of the current window
        max_length = max(max_length, right - left + 1)

    return max_length

s = "eceba"
k = 2

print(lengthOfLongestSubstringKDistinct(s, k))