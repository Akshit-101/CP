
def isOperator(c):
    return c in ['+', '-', '*', '/', '%', '^']


def preToInfix(pre_exp):
    stack = []

    # Process the prefix expression in reverse order
    for c in reversed(pre_exp):
        # If character is an operand, push it to the stack
        if c.isalnum():  # Check if it's a letter or a digit
            stack.append(c)
        # If character is an operator
        elif isOperator(c):
            # Pop two operands from the stack
            op1 = stack.pop()
            op2 = stack.pop()
            # Form a string "(op1 operator op2)" and push it back to the stack
            expression = f"({op1}{c}{op2})"
            stack.append(expression)

    # The final result will be in the stack
    return stack[-1]


pre_exp = "*-A/BC-/AKL"
print("Prefix expression:", pre_exp)
infix_exp = preToInfix(pre_exp)
print("Infix expression:", infix_exp)
