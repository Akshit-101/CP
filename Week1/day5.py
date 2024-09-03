# Valid Parentheses || Approach 1: Stack-Based Method
def isValid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            if stack and stack[-1] == bracket_map[char]:
                stack.pop()
            else:
                return False
    return not stack



# Approach 2: Count-Based Method  (too bad and tooo long :())

def isValid(s: str) -> bool:
    round_count = curly_count = square_count = 0
    for char in s:
        if char == '(':
            round_count += 1
        elif char == ')':
            round_count -= 1
        elif char == '{':
            curly_count += 1
        elif char == '}':
            curly_count -= 1
        elif char == '[':
            square_count += 1
        elif char == ']':
            square_count -= 1
        
        if round_count < 0 or curly_count < 0 or square_count < 0:
            return False
    
    return round_count == 0 and curly_count == 0 and square_count == 0

# Armstrong number || Approach 1: Iterative Method
def isArmstrong(num: int) -> bool:
    digits = str(num)
    n = len(digits)
    sum_of_powers = 0
    
    for digit in digits:
        sum_of_powers += int(digit) ** n
        
    return sum_of_powers == num


# || Approach 2: Mathematical Method  (again too long :())
def isArmstrong(num: int) -> bool:
    original_num = num
    n = 0
    sum_of_powers = 0
    

    temp = num
    while temp > 0:
        temp //= 10
        n += 1
    
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_powers += digit ** n
        temp //= 10
        
    return sum_of_powers == original_num


