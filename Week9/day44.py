def postToPre(post_exp):
    st = []

    # Traverse the postfix expression from left to right
    for ch in post_exp:
        # If the character is an operand, push it to the stack
        if ch.isalnum():
            st.append(ch)
        # If the character is an operator, pop two operands from the stack,
        # form a new prefix expression, and push it back to the stack
        else:
            operand2 = st.pop()
            operand1 = st.pop()
            st.append(ch + operand1 + operand2)

    # The final element in the stack is the prefix expression
    return st[-1]

post_exp = "ABC/-AK/L-*"
print("Prefix expression:", postToPre(post_exp))
