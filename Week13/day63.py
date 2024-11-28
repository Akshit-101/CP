from collections import Counter

def minWindow(s: str, t: str) -> str:
    if not t or not s:
        return ""
    
    # Counting characters in t
    t_count = Counter(t)
    required = len(t_count)
    
    # Sliding window pointers
    left, right = 0, 0
    formed = 0
    window_counts = {}
    
    # Result parameters: (window length, left, right)
    ans = float("inf"), None, None
    
    while right < len(s):
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1
        
        # Checking if this character satisfies the count in t
        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1
        
        # Trying to shrink the window if it's valid
        while left <= right and formed == required:
            char = s[left]
            
            # Saving the smallest window
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)
            
            # Removing the leftmost character and shrink the window
            window_counts[char] -= 1
            if char in t_count and window_counts[char] < t_count[char]:
                formed -= 1
            
            left += 1
        
        # Expanding the window
        right += 1
    
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]

s1 = "ADOBECODEBANC"
t1 = "ABC"
print(minWindow(s1, t1))  # Output: "BANC"

s2 = "a"
t2 = "a"
print(minWindow(s2, t2))  # Output: "a"

s3 = "a"
t3 = "aa"
print(minWindow(s3, t3))  # Output: ""
