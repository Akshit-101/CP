# ------------------------------ Delete Last Node of a Doubly Linked List -----------------------------------

class Node:
    def __init__(self, data, next_node=None, back_node=None):
        self.data = data
        self.next = next_node
        self.back = back_node

def convert_arr_to_dll(arr):
    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i], None, prev)
        prev.next = temp
        prev = temp

    return head

def print_dll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

def delete_tail(head):
    if head is None or head.next is None:
        return None 

    tail = head
    while tail.next is not None:
        tail = tail.next

    new_tail = tail.back
    new_tail.next = None
    tail.back = None

    del tail

    return head

if __name__ == "__main__":
    arr = [12, 5, 8, 7]
    head = convert_arr_to_dll(arr)

    print("Original Doubly Linked List:", end=" ")
    print_dll(head)

    print("\n\nAfter deleting the tail node:", end=" ")
    head = delete_tail(head)
    print_dll(head)


# --------------------------------------- Reverse a Doubly Linked List ----------------------------------------


class Node:
    def __init__(self, data, next_node=None, back_node=None):
        
        self.data = data
        self.next = next_node
        self.back = back_node

def convert_arr_to_dll(arr):
    head = Node(arr[0])
    prev = head

    for i in range(1, len(arr)):
        temp = Node(arr[i], None, prev)
        
        prev.next = temp

        prev = temp

    return head

def print_dll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

def reverse_dll(head):

    if head is None or head.next is None:

        return head
    
    prev = None  

    current = head  
    while current is not None:
        
        prev = current.back 

        current.back = current.next

        current.next = prev 
        
        current = current.back  

    return prev.back

arr = [12, 5, 6, 8, 4]
head = convert_arr_to_dll(arr)
print("\n\nDoubly Linked List Initially:  ")
print_dll(head)

print('Doubly Linked List After Reversing :')

head = reverse_dll(head)
print_dll(head)

