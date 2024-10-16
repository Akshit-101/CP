# ------------------------- Two numbers with odd occurrences -------------------------
def twoOddNum(arr, n):
    xor_all = 0
    for num in arr:
        xor_all ^= num
    
    rightmost_set_bit = xor_all & -xor_all
    
    num1, num2 = 0, 0
    for num in arr:
        if num & rightmost_set_bit:
            num1 ^= num  
        else:
            num2 ^= num 
    
    return sorted([num1, num2], reverse=True)

# Example usage:
arr1 = [4, 2, 4, 5, 2, 3, 3, 1]
arr2 = [1, 7, 5, 7, 5, 4, 7, 4]

print(twoOddNum(arr1, len(arr1)))  # Output: [5, 1]
print(twoOddNum(arr2, len(arr2)))  # Output: [7, 1]


# ------------------------- Two numbers with even occurrences -------------------------


def AllPrimeFactors(N):
    unique_primes = []
    
    if N % 2 == 0:
        unique_primes.append(2)
        while N % 2 == 0:
            N //= 2
    
    for i in range(3, int(N**0.5) + 1, 2):
        if N % i == 0:
            unique_primes.append(i)
            while N % i == 0:
                N //= i
    
    if N > 2:
        unique_primes.append(N)
    
    return unique_primes


N1 = 100
N2 = 35

print(AllPrimeFactors(N1))  # Output: [2, 5]
print(AllPrimeFactors(N2))  # Output: [5, 7]
