# ------------------------------ All divisors of a Number ---------------------------------
def print_divisors(N):
    divisors = []
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            divisors.append(i)
            if i != N // i:
                divisors.append(N // i)
    divisors.sort()
    print(' '.join(map(str, divisors)))

print_divisors(20)   # Output: 1 2 4 5 10 20
print_divisors(21191)  # Output: 1 21191


# ----------------------- Count Primes --------------------------
def countPrimes(n):
    if n < 2:
        return 0
    
    sieve = [True] * n
    sieve[0] = sieve[1] = False  
    
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n, i):
                sieve[j] = False
    
    return sum(sieve)

# Example usage:
print(countPrimes(10))  # Output: 4 (Primes less than 10 are 2, 3, 5, 7)
print(countPrimes(0))   # Output: 0
print(countPrimes(1))   # Output: 0
print(countPrimes(20))  # Output: 8 (Primes less than 20 are 2, 3, 5, 7, 11, 13, 17, 19)