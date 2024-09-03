# Add Two Numbers || Approach 1: Iterative Method
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    
    return dummy.next

# || Approach 2: Recursive Method


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: ListNode, l2: ListNode, carry=0) -> ListNode:
    if not l1 and not l2 and not carry:
        return None
    
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0
    
    total = val1 + val2 + carry
    carry = total // 10
    
    current = ListNode(total % 10)
    
    current.next = addTwoNumbers(l1.next if l1 else None, l2.next if l2 else None, carry)
    
    return current


# Largest product in a series

k = int(input())
n=input()
maxpro=0
for i in range (0, len(n)-k + 1):
    product=int(1)
    for j in range (i,i+k):
        product*=int((n[j]))
    if(product>maxpro):
        maxpro=product

print(maxpro)

#  Summation of Primes

n = int(input())
def iprime(n):
    if n<2:
        return False

    for i in range(2, (n//2)+1):
        if(n%i==0):
            return False

    return True

def suming(n):
    sum = 0
    for i in range(n):
        if iprime(i) == True:
            sum = sum + i
    return sum
ans = suming(n)
print(ans)