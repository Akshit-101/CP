# ----------------------------- Reverse Linked List in groups of Size K -----------------------------

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node
def reverseLinkedList(head):

    temp = head
    prev = None
    
    while temp is not None:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front


    return prev
    

def getKthNode(temp, k):

    k -= 1

    while temp is not None and k > 0:
        k -= 1

        temp = temp.next
    return temp
def kReverse(head, k):
    temp = head

    prevLast = None
    while temp is not None:
        
        kThNode = getKthNode(temp, k)

        if kThNode is None:
            if prevLast:
                prevLast.next = temp

            break

        nextNode = kThNode.next

        kThNode.next = None
        reverseLinkedList(temp)

        if temp == head:
            head = kThNode
        else:
            prevLast.next = kThNode

        prevLast = temp
        temp = nextNode
    return head
def printLinkedList(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(5)
head.next = Node(4)
head.next.next = Node(3)
head.next.next.next = Node(7)
head.next.next.next.next = Node(9)
head.next.next.next.next.next = Node(2)

print("Original Linked List: ", end="")
printLinkedList(head)

head = kReverse(head, 4)
print("Reversed Linked List: ", end="")
printLinkedList(head)

# ----------------------------- Flattening a Linked List -----------------------------

                                
                     
class Node:
    def __init__(self, x=0, nextNode=None, childNode=None):
        self.data = x
        self.next = nextNode
        self.child = childNode

def merge(list1, list2):
    dummyNode = Node(-1)
    res = dummyNode

    while list1 and list2:
        if list1.data < list2.data:
            res.child = list1
            res = list1
            list1 = list1.child
        else:
            res.child = list2
            res = list2
            list2 = list2.child
        res.next = None

    if list1:
        res.child = list1
    else:
        res.child = list2

    if dummyNode.child:
        dummyNode.child.next = None

    return dummyNode.child

def flattenLinkedList(head):

    if not head or not head.next:
        return head

    mergedHead = flattenLinkedList(head.next)
    head = merge(head, mergedHead)
    return head

def printLinkedList(head):
    while head:
        print(head.data, end=" ")
        head = head.child
    print()

def printOriginalLinkedList(head, depth):
    while head:
        print(head.data, end="")

        if head.child:
            print(" -> ", end="")
            printOriginalLinkedList(head.child, depth + 1)

        if head.next:
            print()
            print("| " * depth, end="")
        head = head.next

head = Node(5)
head.child = Node(14)
head.next = Node(10)
head.next.child = Node(4)
head.next.next = Node(12)
head.next.next.child = Node(20)
head.next.next.child.child = Node(13)
head.next.next.next = Node(7)
head.next.next.next.child = Node(17)

print("Original linked list:")
printOriginalLinkedList(head, 0)

flattened = flattenLinkedList(head)
print("\nFlattened linked list: ", end="")
printLinkedList(flattened)

                                
                            

