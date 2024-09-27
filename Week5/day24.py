# ------------------------------ Find middle element in a Linked List ------------------------------

class Node:
    def __init__(self, data, next_node=None):
        self.data = data       
        self.next = next_node  
def find_middle(head):
    slow = head   
    fast = head  
    # the Tortoise and Hare algorithm.
    while fast and fast.next and slow:
        fast = fast.next.next 
        slow = slow.next       

    return slow  


# Creating a sample linked list: 
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

middle_node = find_middle(head)

print("The middle node value is:", middle_node.data)


# 




class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

def reverse_linked_list(head):
    if head is None or head.next is None:
        
        return head

    new_head = reverse_linked_list(head.next)

    front = head.next

    front.next = head

    head.next = None

    return new_head
    
def is_palindrome(head):
    if head is None or head.next is None:
        return True

    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next

        fast = fast.next.next

    new_head = reverse_linked_list(slow.next)

    first = head

    second = new_head
    while second is not None:
        if first.data != second.data:
            
            reverse_linked_list(new_head)
            return False

        first = first.next

        second = second.next

    reverse_linked_list(new_head)

    return True
    
def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()

def main():
    head = Node(1)
    head.next = Node(5)
    head.next.next = Node(2)
    head.next.next.next = Node(5)
    head.next.next.next.next = Node(1)

    print("Original Linked List: ", end="")
    print_linked_list(head)

    if is_palindrome(head):
        print("The linked list is a palindrome.")
    else:
        print("The linked list is not a palindrome.")

if __name__ == "__main__":
    main()

