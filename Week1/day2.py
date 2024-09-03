#  Two Sum problem || Brute Force Approach
def two_sum_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None  # If no solution found

# || Using a Hash Map
def two_sum_optimized(nums, target):
    num_map = {}  
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return None  

# prime number 

def iprime(n):
    if n<2:
        return False

    for i in range(2, (n//2)+1):
        if(n%i==0):
            return False

    return True

# Pentagon numbers

n = int(input())
k = int(input())
arr = []

def pen(n):
    for i in range(1,n+1):
        p = (i*(3*i - 1))//2
        arr.append(p)
    return arr

chu = []
def no(arr):
    for i in range(k,len(arr)):
        x = arr[i] - arr[i - k]
        chu.append(x)
    return chu


def no1(arr):
    for i in range(k,len(arr)):
        x = arr[i] + arr[i - k]
        chu.append(x)
    return chu

def check(arr1 , arr2):
    co = 0
    for i in range(len(arr1)):
        if arr1[i] in arr2:
            co += 1
    return co


a = pen(n)
b = no(a)
c = no1(a)
d = check(c, a)
print(d)


