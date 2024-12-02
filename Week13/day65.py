def maxScore(cardPoints, k):
    n = len(cardPoints)
    total = sum(cardPoints)  # Total sum of all cards
    
    # Edge case: If k equals the length of cardPoints, return the total sum
    if k == n:
        return total

    # Calculating the sum of the subarray of size n - k to leave out
    window_size = n - k
    min_subarray_sum = float('inf')
    current_subarray_sum = 0
    
    # Sliding window to find the smallest subarray sum of size window_size
    for i in range(n):
        current_subarray_sum += cardPoints[i]
        if i >= window_size - 1:
            min_subarray_sum = min(min_subarray_sum, current_subarray_sum)
            current_subarray_sum -= cardPoints[i - window_size + 1]

    return total - min_subarray_sum


cardPoints1 = [1, 2, 3, 4, 5, 6, 1]
k1 = 3
print(maxScore(cardPoints1, k1))  # Output: 12

cardPoints2 = [2, 2, 2]
k2 = 2
print(maxScore(cardPoints2, k2))  # Output: 4

