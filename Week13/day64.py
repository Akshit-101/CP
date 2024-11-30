# Question: Minimum Window Subsequence

# You are given two strings s1 and s2 of lengths m and n, respectively. You need to find the minimum window subsequence in s1 such that s2 is a 
# subsequence of the window.
# If there is no such window in s1 that covers s2, return an empty string "". If there are multiple minimum windows, return the one with the 
# smallest starting index. 

def minWindowSubsequence(s1: str, s2: str) -> str:
    m, n = len(s1), len(s2)
    start, min_len = 0, float('inf')

    # Helper function to find the end of the window containing s2 as a subsequence
    def findSubsequenceStart(i):
        j = 0
        while i < m:
            if s1[i] == s2[j]:
                j += 1
                if j == n:
                    return i  # Found the end index
            i += 1
        return -1

    # Process the subsequence and find the minimum window
    i = 0
    while i < m:
        end = findSubsequenceStart(i)
        if end == -1:
            break

        # Backtrack to find the start index of the valid window
        j = end
        k = n - 1
        while k >= 0:
            if s1[j] == s2[k]:
                k -= 1
            j -= 1

        j += 1  # Adjust to include the character at j
        if end - j + 1 < min_len:
            start, min_len = j, end - j + 1

        # Move `i` forward for the next window search
        i = j + 1

    return "" if min_len == float('inf') else s1[start:start + min_len]


# Example Usage
s1 = "abcdebdde"
s2 = "bde"
result1 = minWindowSubsequence(s1, s2)
print(f"Result for s1 = '{s1}' and s2 = '{s2}': {result1}")  # Expected: "bcde"

s1 = "jmeqksfrsdcmsiwvaovztaqenprpvnbstl"
s2 = "k"
result2 = minWindowSubsequence(s1, s2)
print(f"Result for s1 = '{s1}' and s2 = '{s2}': {result2}")  # Expected: "k"


