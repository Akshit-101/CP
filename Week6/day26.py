def generateParenthesis(n):
    result = []

    def backtrack(current_string, open_count, close_count):
        # If the current string has reached the maximum length (2 * n), add to results
        if len(current_string) == 2 * n:
            result.append(current_string)
            return
        
        # If we can add an opening bracket, add it and recurse
        if open_count < n:
            backtrack(current_string + "(", open_count + 1, close_count)
        
        # If we can add a closing bracket, add it and recurse
        if close_count < open_count:
            backtrack(current_string + ")", open_count, close_count + 1)
    
    # Initial call to the backtracking function
    backtrack("", 0, 0)
    return result

n = 3
print(generateParenthesis(n))
