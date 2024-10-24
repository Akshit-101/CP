def preToPost(pre_exp):
    st = []

    # Read the prefix expression from R to L
    for ch in reversed(pre_exp):
        # If the current character is an operand, push it to the stack
        if ch.isalnum():
            st.append(ch)
        # If the current character is an operator, pop two operands from the stack,
        # create a new postfix expression, and push it back to the stack
        else:
            operand1 = st.pop()
            operand2 = st.pop()
            st.append(operand1 + operand2 + ch)

    # The final element in the stack is the postfix expression
    return st[-1]


pre_exp = "*-A/BC-/AKL"
print("Postfix expression:", preToPost(pre_exp))
