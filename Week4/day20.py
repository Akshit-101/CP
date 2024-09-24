# -------------------------------------- String to Integer (atoi) --------------------------------------

def myAtoi(s: str) -> int:
    s = s.lstrip()
    if not s:
        return 0

    sign = 1
    start_index = 0
    
    if s[0] == '-':
        sign = -1
        start_index = 1
    elif s[0] == '+':
        start_index = 1
    
    result = 0
    for i in range(start_index, len(s)):
        if not s[i].isdigit():
            break
        result = result * 10 + int(s[i])
    
    result *= sign
    
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    if result < INT_MIN:
        return INT_MIN
    if result > INT_MAX:
        return INT_MAX
    
    return result

print(myAtoi("   -42")) 
print(myAtoi("00000123"))  

# -------------------------------------- Count number of substrings --------------------------------------

from collections import defaultdict

def substrCount(S: str, K: int) -> int:
    def atMostK(S, K):
        count = 0
        left = 0
        freq_map = defaultdict(int)

        for right in range(len(S)):
            freq_map[S[right]] += 1
            
            while len(freq_map) > K:
                freq_map[S[left]] -= 1
                if freq_map[S[left]] == 0:
                    del freq_map[S[left]]
                left += 1
            
            count += (right - left + 1)
        return count
    return atMostK(S, K) - atMostK(S, K - 1)

print(substrCount("ababab", 2))    
print(substrCount("abcabcabc", 3))  