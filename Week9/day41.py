# Function to return precedence of operators
def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def infixToPostfix(s):
    st = []  # Using a list as a stack in Python
    result = ""

    for c in s:
        # If the scanned character is an operand, add it to the output string
        if c.isalnum():  # Checks if it's a letter or a digit
            result += c

        # If the scanned character is an '(' push it to the stack
        elif c == '(':
            st.append('(')

        # If the scanned character is a ')', pop and add to the output
        # until '(' is encountered
        elif c == ')':
            while st and st[-1] != '(':
                result += st.pop()
            st.pop()  # Pop the '(' from the stack

        # If an operator is encountered
        else:
            while st and prec(c) <= prec(st[-1]):
                result += st.pop()
            st.append(c)

    # Pop all the remaining operators from the stack
    while st:
        result += st.pop()

    print("Postfix expression:", result)

exp = "(p+q)*(m-n)"
print("Infix expression:", exp)
infixToPostfix(exp)
