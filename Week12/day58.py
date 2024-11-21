def totalFruit(arr):
    left = 0
    max_fruits = 0
    fruit_count = {}

    for right in range(len(arr)):
        fruit_count[arr[right]] = fruit_count.get(arr[right], 0) + 1

        while len(fruit_count) > 2:
            fruit_count[arr[left]] -= 1
            if fruit_count[arr[left]] == 0:
                del fruit_count[arr[left]]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits

arr1 = [2, 1, 2]
print(totalFruit(arr1))  # Output: 3

arr2 = [3, 1, 2, 2, 2, 2]
print(totalFruit(arr2))  # Output: 5
