def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Example usage
sorted_list = [1, 3, 5, 7, 9, 11]
print(binary_search(sorted_list, 7))  # Output: 3
print(binary_search(sorted_list, 4))  # Output: -1


# Why?
# This snippet implements a binary search algorithm, which is a fundamental concept in computer science.
# It’s efficient (O(log n)) and widely used for searching in sorted datasets, making it essential for algorithms and
# data structure enthusiasts.
