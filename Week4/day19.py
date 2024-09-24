# ------------------------------------ Sort Characters by frequency ------------------------------------

from collections import Counter

def frequencySort(s: str) -> str:
    # Count the frequency of each character
    freq_map = Counter(s)
    
    # Sort characters by frequency in descending order
    sorted_chars = sorted(freq_map, key=lambda x: freq_map[x], reverse=True)
    
    #  Build the result string by repeating characters based on their frequency
    result = ''.join([char * freq_map[char] for char in sorted_chars])
    
    return result
print(frequencySort("tree"))  

# ----------------------------- Roman Number to Integer and vice versa ---------------------------------

def romanToInt(s: str) -> int:
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0

    for i in range(len(s)):
        if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:
            total -= roman_map[s[i]]
        else:
            total += roman_map[s[i]]
    
    return total

print(romanToInt("III")) 
print(romanToInt("MCMXCIV"))