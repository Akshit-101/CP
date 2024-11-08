# -----------------------------------------
def postToInfix(post_exp):
    st = []

    # Traverse the postfix expression
    for ch in post_exp:
        # If operand, push it to stack
        if ch.isalnum():
            st.append(ch)
        else:
            # Pop two operands, form the infix expression, and push it back
            operand2 = st.pop()
            operand1 = st.pop()
            st.append(f"({operand1}{ch}{operand2})")
    
    # The last element in stack is the infix expression
    return st[-1]

post_exp = "ab*c+"
print("Infix expression:", postToInfix(post_exp))

# -----------------------------------------


def precedence(op):
    if op == '^':
        return 3
    elif op == '/' or op == '*':
        return 2
    elif op == '+' or op == '-':
        return 1
    else:
        return -1

def infixToPrefix(infix_exp):
    # Step 1: Reverse the infix expression
    infix_exp = infix_exp[::-1]
    st = []
    result = ""

    for ch in infix_exp:
        # If operand, add to result
        if ch.isalnum():
            result += ch
        # If ')', push to stack
        elif ch == ')':
            st.append(ch)
        # If '(', pop until ')' and add to result
        elif ch == '(':
            while st and st[-1] != ')':
                result += st.pop()
            st.pop()
        else:
            # Pop all operators of higher precedence from stack and add to result
            while st and precedence(ch) < precedence(st[-1]):
                result += st.pop()
            st.append(ch)
    
    # Pop all remaining operators
    while st:
        result += st.pop()
    
    # Reverse result for final prefix expression
    return result[::-1]


infix_exp = postToInfix(post_exp)
print("Prefix expression:", infixToPrefix(infix_exp))


