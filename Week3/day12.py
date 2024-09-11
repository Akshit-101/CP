# ------------------------------- Merge Sort Algorithm ----------------------------------

def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

if __name__ == "__main__":
    arr = [4, 2, 1, 6, 7]
    print("Before Sorting:", arr)
    merge_sort(arr, 0, len(arr) - 1)
    print("After Sorting:", arr)


# ------------------------------- Merge Sort Algorithm ----------------------------------

# Function to perform Bubble Sort recursively
def bubble_sort(arr, n):
    # Base Case: if there's only one element, it's already sorted >> :) ....
    if n == 1:
        return

    did_swap = False  # Track if any swapping occurs in this pass ????

    # Perform one pass of Bubble Sort......
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]  # Swap
            did_swap = True

    # If no swapping happened, the array is already sorted :)
    if not did_swap:
        return

    # Recur for the next pass with one fewer element
    bubble_sort(arr, n - 1)

if __name__ == "__main__":
    arr = [13, 46, 24, 52, 20, 9]
    print("Before Sorting:", arr)
    
    bubble_sort(arr, len(arr))
    
    print("After Sorting:", arr)
