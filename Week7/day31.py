	
# ----------------------------- Check if a number is power of 2 or not -----------------------------

def isPowerOfTwo(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0
# The key logic: If n is a power of two, it has exactly one '1' in its binary form
# For example, for n = 16 (binary 10000), n-1 = 15 (binary 01111)
# Performing a bitwise AND between n and n-1 will give 0 if n is a power of two
# Because there are no common set bits between n and n-1 in such cases
# If n & (n - 1) == 0, it's a power of two


# -------------------------- Divide two integers without using multiplication, division and mod operator -----------------

def divide(dividend: int, divisor: int) -> int:
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX
    
    negative = (dividend < 0) != (divisor < 0)
    
    dividend, divisor = abs(dividend), abs(divisor)
    
    quotient = 0
    
    # Bit-shifting to subtract large multiples of the divisor
    while dividend >= divisor:
        temp_divisor, multiple = divisor, 1
        # Shift left (double the divisor) until it exceeds the dividend
        while dividend >= (temp_divisor << 1):
            temp_divisor <<= 1
            multiple <<= 1
        # Subtract the largest shifted divisor from the dividend
        dividend -= temp_divisor
        # Add the corresponding multiple to the quotient
        quotient += multiple
    
    # Appling the sign to the result
    quotient = -quotient if negative else quotient
    
    return min(max(INT_MIN, quotient), INT_MAX)


dividend = 10
divisor = 3
print(divide(dividend, divisor))  

dividend = 7
divisor = -3
print(divide(dividend, divisor))  
