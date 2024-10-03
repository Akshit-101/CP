# ---------------------------- Reverse a stack using recursion ----------------------------

def insert_at_bottom(stack, element):
    if len(stack) == 0:
        stack.append(element)
    else:
        top = stack.pop()
        insert_at_bottom(stack, element)
        stack.append(top)

def Reverse(stack):
    if len(stack) == 0:
        return
    top = stack.pop()
    Reverse(stack)
    insert_at_bottom(stack, top)

stack = [3, 2, 1, 7, 6]
Reverse(stack)
print(stack)  


# ---------------------------- Sort a stack using recursion ----------------------------

def insert_sorted(stack, element):
    if len(stack) == 0 or stack[-1] <= element:
        stack.append(element)
    else:
        top = stack.pop()
        insert_sorted(stack, element)
        stack.append(top)


def sort(stack):
    if len(stack) != 0:
        top = stack.pop()
        sort(stack)
        insert_sorted(stack, top)


stack = [11, 2, 32, 3, 41]
sort(stack)
print(stack)  

