def removeOuterParentheses(s: str) -> str:
    result = []
    balance = 0
    
    for char in s:
        if char == '(':
            if balance > 0:
                result.append(char)  # Only append if it's not the outermost '('
            balance += 1
        else:  # char == ')'
            balance -= 1
            if balance > 0:
                result.append(char)  # Only append if it's not the outermost ')'
    
    return ''.join(result)

print(removeOuterParentheses("(()())(())"))          
print(removeOuterParentheses("(()())(())(()(()))"))   
print(removeOuterParentheses("()()"))                 
