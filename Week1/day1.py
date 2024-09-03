# Practicing syntax by solving some basic questions.

# Sum of extracted digits

n1 = int(input())
n2 = int(input())
if n1>=10 and n2>=10:
  z = int(n2/10)
  b = z%10  
  x = int(n1/10)
  a = x%10
  print(a+b)
else:
    print("Invalid number")  

# Display a matrix of m*n size (revising 'for loop')

m,n=map(int, input().split())
for i in range(m):
  print("") # or print()
  for j in range (n):
     print("1",end=" ")


# Remove duplicates from subarray
n = int(input())
arr = list(map(int, input().split()))
co = 0
s = ""
for i in arr:
    x = str(i)
    s += x

for i in range (len(s)):
    for j in range(len(s)):
        if s[i] == s[j] and i != j:
            a = s[i]
            s = s.replace(str(a), "#",1)

for i in s:
    if i == "#":
        co += 1

print(n - co)

# List Comprehensions
squares = [x**2 for x in range(10)]
print(squares)


# Object Oriented Programming
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy", "Golden Retriever")
print(my_dog.bark())
