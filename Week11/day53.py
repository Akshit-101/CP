def findCelebrity(n):
    stack = [i for i in range(n)]
    
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        
        # Check if a knows b
        if knows(a, b):
            # a can't be a celebrity, but b might be
            stack.append(b)
        else:
            # b can't be a celebrity, but a might be
            stack.append(a)
    
    # If there's no one in the stack, returning -1
    if not stack:
        return -1
    
    # Verify's if the last person is a celebrity
    candidate = stack.pop()
    for i in range(n):
        # A candidate should not know anyone and everyone should know the candidate
        if (i != candidate and (knows(candidate, i) or not knows(i, candidate))):
            return -1
    
    return candidate

def knows(a, b):
    return relationships[a][b]
relationships = [
    [False, True, True],  
    [False, False, True], 
    [False, False, False] 
]
n = 3
print(findCelebrity(n)) 
